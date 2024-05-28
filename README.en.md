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


## Automated Checks and Testing

Below are described the procedures for automated checks and testing implemented, essential for ensuring the quality and integrity of the repository content.

### Automated Checks (Pre-commit)

This repository implements automated checks using [pre-commit](https://pre-commit.com/). The specifications of the checks are defined in the file [`.pre-commit-config.yaml`](.pre-commit-config.yaml).

These checks can be executed using GitHub Actions. The `validate.yaml` file in `.github/workflows` automatically enables pre-commit checks after each push or pull request (PR). Additionally, these checks can be manually activated at any time.

To enable pre-commit checks in another repository, simply copy the [`.pre-commit-config.yaml`](.pre-commit-config.yaml) file and the [`.github/workflows/validate.yaml`](.github/workflows/validate.yaml) file.

### URL Testing

In the `tests` directory, there is a script named `test_urls.py`, which verifies GitHub-related URLs present in the files of the `assets` subdirectories.

This test can also be automated using GitHub Actions. The `test.yaml` file in `.github/workflows` automatically activates tests after each push or pull request. Similarly, these tests can be manually initiated at any time.

To enable URL testing in another repository, simply copy the [`/tests/test_urls.py`](/tests/test_urls.py) file and the [`.github/workflows/test.yaml`](.github/workflows/test.yaml) file.

### Local Checks and Testing

Local checks and testing can be performed using Docker or simply Python. An integrated test environment to reproduce the CI pipeline is available through `docker-compose`, which executes a series of steps.

```bash
docker-compose -f docker-compose-test.yml up
```

Note: If you wish to transfer this environment to another repository, it's important to note that the Docker environment requires the Dockerfiles present in the tests directory (such as Dockerfile.precommit and Dockerfile.pytest).