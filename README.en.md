# Template repository for semantic assets

This is a template repository for semantic assets to be harvested
by the National Data Catalog at https://schema.gov.it.

For further information on the Catalog, on how to use the portal 
schema.gov.it, and on contributing to its content, please refer 
to the [dedicated guide](https://teamdigitale.github.io/dati-semantic-guida-ndc-docs/).

## Repository layout and rules

This section describes the general layout of a semantic
repository.

All semantic assets are in the [assets](assets/) folder,
each asset type (e.g. ontologies, controlled vocabularies, schemas, ..)
has a proper sub-folder.

For readability:

- all json files are serialized as yaml;
- all RDF files are serialized as text/turtle;
- all semantic assets to be harvested/published are in assets/;
  files outside this directory should be safely ignored by other entities
  and are either used for testing or for developing and validating what's in assets/.

To delve deeper into the topic of the repository layout, the required content, 
the versioning of resources, and to consult some useful examples, please refer 
to the 
[dedicated section in the Operational Manual of the Catalog](https://teamdigitale.github.io/dati-semantic-guida-ndc-docs/docs/manuale-operativo/istruzioni-su-come-predisporre-il-repository-in-cui-pubblicare-le-risorse-semantiche.html).


## Automatic Checks and Tests

This section describes the automatic check and test procedures 
used to ensure the quality and integrity of the repository content.

### Automatic Checks (Pre-commit)

This repository uses [pre-commit](https://pre-commit.com/) 
for automatic checks. The checks are specified 
in the [`.pre-commit-config.yaml`](.pre-commit-config.yaml) file.

These checks can be run via GitHub Actions. 
The `validate.yaml` file in `.github/workflows` 
automatically enables pre-commit checks after each push or pull request (PR). 
You can also run them manually at any time.

To enable pre-commit checks in another repository, 
copy the [`.pre-commit-config.yaml`](.pre-commit-config.yaml) file 
and the [`.github/workflows/validate.yaml`](.github/workflows/validate.yaml) file.

Note: It is possible to comment on checks deemed unnecessary or inappropriate. For example, when using a solution with stable URIs, the validation check of the filename against the URIs (validate-filename-match-uri) may not be essential.

### URL Tests

The `test_urls.py` script in the `tests` directory verifies 
GitHub-related URLs in the `assets` subdirectory files.

This test can also be automated using GitHub Actions. 
The `test.yaml` file in `.github/workflows` 
automatically runs the tests after each push or pull request. 
You can also run them manually at any time.

To enable URL tests in another repository, 
copy the [`/tests/test_urls.py`](/tests/test_urls.py) file 
and the [`.github/workflows/test.yaml`](.github/workflows/test.yaml) file.

### Local Checks and Tests

Checks and tests can also be run locally 
using Docker or Python. Use `docker-compose` 
to replicate the CI pipeline:

```bash
docker-compose -f docker-compose-test.yml up
```

Note: To transfer this environment to another repository,
include the Dockerfiles in the `tests` directory
(such as `Dockerfile.precommit` and `Dockerfile.pytest`).