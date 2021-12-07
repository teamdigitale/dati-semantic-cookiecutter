# Modello di repository per risorse semantiche

Questo è un repository template per le risorse semantiche da raccogliere
dal catalogo dei dati nazionali erogato su https://schema.gov.it.

## Layout e regole del repository

Questa sezione descrive il l'alberatura generale di un
Repository semantico.
Le regole di dettaglio sono in [CONTRIBUTING.md](CONTRIBUTING.md).

Tutte le risorse semantiche sono nella cartella [asset](assets/),
Ogni tipo di risorsa (ad esempio ontologie, vocabolari controllati, schemi, ..)
ha una sottocartella specifica.

Per la leggibilità:

- Tutti i file JSON sono serializzati come YAML;
- Tutti i file RDF sono serializzati come  `text/turtle`;
- tutte le risorse semantiche da raccogliere / pubblicare sono in `assets/`;
  I file al di fuori di questa directory vengono ignorati dal catalogo
  e possono essere utilizzati per testare, sviluppare e convalidare i contenuti di  `assets/`.

## Sviluppo

Questo repository utilizza [pre-commit](https://pre-commit.com/) per convalidare il contenuto dei file:
le verifiche sono indicate in [.pre-commit-config.yaml](.pre-commit-config.yaml).

Un ambiente di test integrato per riprodurre la pipeline CI
è disponibile tramite docker-compose, che esegue una serie di passaggi.

```bash
docker-compose -f docker-compose-test.yml up
```
