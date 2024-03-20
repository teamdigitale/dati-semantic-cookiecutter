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


## Controlli Automatici e Test

Di seguito vengono descritte le procedure di controllo automatico e di test implementate, utili per garantire la qualità e l'integrità del contenuto del repository

### Controlli Automatici (Pre-commit)

Questo repository implementa i controlli automatici utilizzando [pre-commit](https://pre-commit.com/). Le specifiche delle verifiche sono definite nel file [`.pre-commit-config.yaml`](.pre-commit-config.yaml).

È possibile eseguire tali verifiche mediante GitHub Actions. Il file `validate.yaml` in `.github/workflows` abilita automaticamente i controlli pre-commit dopo ogni push o pull request (PR). Inoltre, è possibile attivare manualmente tali controlli in qualsiasi momento.

Per abilitare i controlli pre-commit in un altro repository, è sufficiente copiare il file [`.pre-commit-config.yaml`](.pre-commit-config.yaml) e il file [`.github/workflows/validate.yaml`](.github/workflows/validate.yaml).

### Test URL

Nella directory `tests` è presente uno script denominato `test_urls.py`, che consente di verificare gli URL relativi a GitHub presenti nei file delle sottodirectory `assets`.

Anche questo test può essere automatizzato mediante GitHub Actions. Il file `test.yaml` in `.github/workflows` attiva automaticamente i test dopo ogni push o pull request. Allo stesso modo, è possibile avviare manualmente questi test in qualsiasi momento.

Per abilitare i test URL in un altro repository, è sufficiente copiare il file [`/tests/test_urls.py`](/tests/test_urls.py) e il file [`.github/workflows/test.yaml`](.github/workflows/test.yaml).

### Controlli e Test in Locale

È possibile eseguire i controlli e i test in locale utilizzando l'ambiente Docker o semplicemente Python. Un ambiente di test integrato per riprodurre la pipeline CI è disponibile tramite `docker-compose`, che esegue una serie di passaggi.

```bash
docker-compose -f docker-compose-test.yml up
```

Nota: Se si desidera trasferire questo ambiente su un altro repository, è importante considerare che l'ambiente Docker richiede i Dockerfile presenti nella directory `tests` (come `Dockerfile.precommit` e `Dockerfile.pytest`).

