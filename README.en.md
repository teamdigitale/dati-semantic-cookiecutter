# Template repository for semantic assets

This is a template repository for semantic assets to be harvested
by the National Data Catalog at https://schema.gov.it.

## Repository layout and rules

This section describes the general layout of a semantic
repository.
For a detailed set of rules regarding this repository
see CONTRIBUTION.md.

All semantic assets are in the [assets](assets/) folder,
each asset type (e.g. ontologies, controlled vocabularies, schemas, ..)
has a proper sub-folder.

For readability:

- all json files are serialized as yaml;
- all RDF files are serialized as text/turtle;
- all semantic assets to be harvested/published are in assets/;
  files outside this directory should be safely ignored by other entities
  and are either used for testing or for developing and validating what's in assets/.


## Development

This repository uses pre-commit to validate content.
An integrated testing environment to reproduce the CI pipeline
is available via docker-compose, which goes on thru a set of steps.

```bash
docker-compose -f docker-compose-test.yml up
```
