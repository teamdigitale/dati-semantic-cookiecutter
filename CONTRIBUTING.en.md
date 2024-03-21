# Contributing assets to the National Data Catalog

This document defines the guidelines for contributing
assets to the National Data Catalog using harvested
repositories.

## Requirements Notation

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT",
"RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL"
in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when,
and only when, they appear in all capitals, as shown here.

## Required files and repository layout

The repository MUST contain the following files:

- ndc-config.yaml: referencing the location of the semantic assets;
- publiccode.yaml: containing all the information required by the
  reuse catalog.

All contributed assets MUST reside inside the `assets/` folder
referenced in ndc-config.yaml.
Assets outside `assets/` will not be processed.

Each asset type (ontologies, controlled vocabularies, schemas)
MUST reside in its specific folder with a pre-defined name,
referenced in ndc-config.yaml.

File and folder names MUST match
the following pattern `[a-zA-Z0-9_-.]{,64}`.
Spaces MUST not be used in files or directory names.
Folders SHOULD be lowercase.

The name of each file MUST match the name of the corresponding resource in the URI used to reference it.
The names of the files in a directory MUST match the name of the directory that contains them, except for their extensions.

In addition, `htaccess` files that define the redirect rules of the URIs MUST be created and published on the w3id repository, as described in [REDIRECT.md](REDIRECT.md).

Assets content MUST be encoded in UTF-8 or ASCII.

Each asset MUST reside under its specific folder:

- ontologies: in `assets/ontologies/`;
- controlled vocabularies: in `assets/controlled-vocabularies/`;
- schemas: in `assets/schemas/`.

For example, the `MyOntology` path will be `assets/ontologies/MyOnto/`.

### Documentation files

Asset folders MAY contain documentation
files in markdown format.
File extension MUST be `.md` (e.g. `README.md`).
Those files will not be processed.

### Versioning folders

Asset folders MAY be structured with further subfolders
to support versioning. Subfolders name MUST match the following
pattern: `(latest|v?[0-9]+(\.[0-9]+){0,2})`.
An asset folder MUST not contain version subfolders mixing
version with and without the `v` prefix.

Three examples of valid sub-folder names:

```
assets/ontologies/CPV/v0.4.2
assets/ontologies/CPV/0.5
assets/schemas/Person/latest
```

The harvester only process:

- the `latest` folder if present;
- the folder with the higher version according to
  semantic versioning.

Ontology folders MUST NOT contain
RDF resources in other serializations
(e.g. rdf/xml, json-ld, ..) since they
will not be processed.
Those files can be placed in the same
repository outside the `assets/` folder
and SHOULD be generated automatically
from the original files in `assets/`.

### No Alternative RDF Representations

Asset folders MUST NOT contain
RDF resources in other serializations
(e.g. rdf/xml, json-ld, ..) since they
will not be processed.

Those files can be placed in the same
repository outside the `assets/` folder;
in this case, they
SHOULD be generated automatically
from the original files in `assets/`.

## Ontologies

Published ontologies MUST conform to the associated
National Guidelines.

Ontologies MUST be published only in RDF/Turtle format
(media-type `text/turtle`).
This is because this format is human-readable.
File extension MUST be `.ttl`.

Ontology folders MAY contain documentation
files in markdown format.
File extension MUST be `.md` (e.g. `README.md`).
Those files will not be processed.

## Controlled Vocabularies

Published controlled vocabularies MUST conform to the associated
National Guidelines.

Controlled Vocabularies MUST be published in RDF/Turtle format
(media-type `text/turtle`).
This is because this format is human-readable.
File extension MUST be `.ttl`.

Controlled Vocabulary folders SHOULD contain
one csv representation of the vocabulary
together with the metadata required to map the csv fields
to the RDF properties:
this representation will be exposed by the NDC via REST APIs.
File extension MUST be `.csv`.

## Schemas

Published schemas MUST conform to the associated
National Guidelines.

Schemas for OAS3 APIs MUST be published in OpenAPI3 format,
embedded in the `#/components/schemas` section of the OAS file.
File extension MUST be `.oas3.yaml`.

The associated metadata MUST be published in
RDF/Turtle format
(media-type `text/turtle`).
File extension MUST be `.ttl`.
This file SHOULD be generated automatically
from the yaml file.

Provided schemas can be validated using the tool
provided on [OpenAPI-Validator](https://italia.github.io/api-oas-checker).

## Quality Checks

The repository SHOULD be checked for quality issues
using continuous integration tools such as github-actions or
github-ci.
