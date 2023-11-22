# Modello di repository per risorse semantiche

Questo è un repository template per le risorse semantiche da raccogliere
dal catalogo dei dati nazionali erogato su https://schema.gov.it.

## Layout e regole del repository

Questa sezione descrive l'alberatura generale di un
Repository semantico.
Le regole di dettaglio sono in [CONTRIBUTING.md](CONTRIBUTING.md).

Tutte le risorse semantiche sono nella cartella [asset](assets/),
Ogni tipo di risorsa (ad esempio ontologie, vocabolari controllati, schemi, ..)
ha una sottocartella specifica.

Per la leggibilità:

- Tutti i file JSON sono serializzati come YAML;
- Tutti i file RDF sono serializzati come  `text/turtle`;

### Asset semantici (schemi, vocabolari, ontologie)

Tutte le risorse semantiche da raccogliere / pubblicare sono in `assets/`;
I file al di fuori di questa directory vengono ignorati dal catalogo
e possono essere utilizzati per testare, sviluppare e convalidare i contenuti di  `assets/`,
come ad esempio i file presenti in [tests/](tests/).

### Altri file

In questo repository, file ulteriori che non devono essere processati
dal NDC sono nella directory [other/](other/), per la quale non è definita
un'alberatura specifica.

In questa directory è possibile anche inserire file che vengono pubblicati
direttamente tramite questo repository (e.g. ulteriori serializzazioni RDF,
schemi ancillari, vocabolari specifici) che non devono essere processati
dal NDC ma che possono comunque essere referenziati dagli oggetti indicizzati
come:

- documentazione in formato pdf;
- ulteriori dataset o schemi di dati;
- immagini e software.



## Sviluppo

Questo repository utilizza [pre-commit](https://pre-commit.com/) per convalidare il contenuto dei file:
le verifiche sono indicate in [.pre-commit-config.yaml](.pre-commit-config.yaml).

Un ambiente di test integrato per riprodurre la pipeline CI
è disponibile tramite docker-compose, che esegue una serie di passaggi.

```bash
docker-compose -f docker-compose-test.yml up
```
