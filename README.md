# Repository per sperimentare con risorse semantiche

Questo è un repository dove effettuare esperimenti con risorse semantiche
per individuare delle strategie utili a raccogliere e pubblicare asset
sul catalogo dei dati nazionali erogato su schema.gov.it.

Per ulteriori informazioni:

- [Come pubblicare risorse semantiche su schema.gov.it](https://github.com/teamdigitale/dati-semantic-guida-ndc-docs)
- [Template per repository con risorse semantiche](https://github.com/teamdigitale/dati-semantic-cookiecutter)


## Validatori

Questo repository contiene una serie di pre-commit hooks utili
a validare risorse semantiche, e viene utilizzato per la CI
di [Ontopia](https://github.com/italia/daf-ontologie-vocabolari-controllati/).
Vedi ad esempio il [file di configurazione](https://github.com/italia/daf-ontologie-vocabolari-controllati/blob/master/.github/workflows/ci-onto.yaml)

## Layout e regole del repository

Questa sezione descrive il l'alberatura generale di un
Repository semantico.
Le regole di dettaglio sono sul repository [guida-ndc](https://github.com/teamdigitale/dati-semantic-guida-ndc-docs).

Tutte le risorse semantiche sono nella cartella [asset](assets/),
Ogni tipo di risorsa (ad esempio ontologie, vocabolari controllati, schemi, ..)
ha una sottocartella specifica.

Per la leggibilità:

- Tutti i file JSON sono serializzati come YAML. Stiamo [lavorando col W3C](https://github.com/json-ld/yaml-ld/) 
  per standardizzare l'uso di YAML in campo semantico usando l'estensione `.yamlld`;
- Tutti i file RDF sono serializzati come  `text/turtle` e hanno estensione `.ttl`;
- tutte le risorse semantiche da raccogliere / pubblicare sono in `assets/`;
  I file al di fuori di questa directory vengono ignorati dal catalogo
  e possono essere utilizzati per testare, sviluppare e convalidare i contenuti di  `assets/`.

## Sviluppo

Questo repository utilizza [pre-commit](https://pre-commit.com/) per convalidare il contenuto dei file:
le verifiche sono indicate in [.pre-commit-config.yaml](.pre-commit-config.yaml).

Un ambiente di test integrato per riprodurre la pipeline CI
è disponibile tramite docker-compose, che esegue una serie di passaggi
customizzabili a seconda dei casi d'uso.

```bash
docker-compose -f docker-compose-test.yml up
```


C'è poi l'ambiente di base che lancia due container coi servizi
ed un container (che poi termina) per i test di pre-commit.

```bash
docker-compose up
```