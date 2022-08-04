import json
from pathlib import Path

import pytest
import yaml
from frictionless import Package, Resource
from frictionless.plugins.csv import CsvDialect
from frictionless.plugins.json import JsonDialect
from pyld import jsonld
from rdflib import Graph

vocab_name = "education-level"


@pytest.fixture
def vocab_rdf():
    return f"{vocab_name}.ttl"


def yaml_load(yaml_file):
    with open(yaml_file, "r") as f:
        return yaml.safe_load(f)


def rdf_as_dict(vocab_rdf):
    g = Graph()
    g.parse(vocab_rdf, format="text/turtle")
    vocab_json = g.serialize(format="application/ld+json")
    return yaml.safe_load(vocab_json)


def _setize(s):
    if isinstance(s, list):
        return set(s)
    elif isinstance(s, str):
        return {
            s,
        }
    return {}


def vocab_frame(vocab_rdf):
    vocab_dict = rdf_as_dict(vocab_rdf)
    frame = yaml_load(f"{vocab_name}.frame.yamlld")
    data = jsonld.frame(vocab_dict, frame=frame)
    _types = _setize(frame["@type"])
    if "@type" in frame:
        data["@graph"] = [
            x.__delitem__("@type") or x
            for x in data["@graph"]
            if _types < _setize(x.get("@type", []))
        ]
    return data


def test_frame(vocab_rdf):
    data = vocab_frame(vocab_rdf)
    Path("vocabulary.tmp.json").write_text(json.dumps(data["@graph"], indent=2))
    assert data["@graph"]
    assert data["@context"]


@pytest.fixture
def mock_csv(vocab_rdf):
    json_ld = vocab_frame(vocab_rdf)
    dpath = f"{vocab_name}.tmp.csv"
    ld_to_csv(json_ld, dpath)
    return dpath


def test_f10s_datapackage():
    package = Package("datapackage.json")
    package.validate()
    for resource in package.resources:
        resource.validate()
        data = resource.read_rows()
        assert len(data) == len(Path(resource.path).read_text().splitlines()) - bool(
            resource.header
        )


def test_csv(vocab_rdf):
    json_ld = vocab_frame(vocab_rdf)
    dpath = f"{vocab_name}.tmp.csv"
    ld_to_csv(json_ld, dpath)
    assert Path(dpath).exists()


def ld_to_csv(json_ld, dpath):
    # Import with f10s.
    resource = Resource(data=json_ld["@graph"], dialect=JsonDialect(keyed=True))
    resource.validate()
    resource.write(
        dpath,
        dialect=CsvDialect(
            delimiter=",",
        ),
    )


from flask import request

package = Package("datapackage.json")
package.validate()
for resource in package.resources:
    resource.validate()
    data = resource.read_rows()
    context = resource["schema"]["x-jsonld-context"]


def list_entries():
    json_ld = {
        "@context": context,
        "@graph": data,
    }
    accept = request.headers.get("Accept")
    if accept == "text/turtle":
        g = Graph()
        g.parse(data=json_ld, format="application/ld+json")
        ret = g.serialize(format="text/turtle")
        print(ret)
        return ret
    return json_ld
