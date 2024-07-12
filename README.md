# Modello di repository per risorse semantiche

Questo è un repository template per le risorse semantiche da raccogliere
dal Catalogo Nazionale Dati per l'interoperabilità erogato su https://schema.gov.it.

Per reperire ulteriori informazioni sul Catalogo, 
sulle modalità di fruizione del portale schema.gov.it e sulla contribuzione
all'alimentazione dello stesso, fai riferimento alla 
[guida dedicata](https://teamdigitale.github.io/dati-semantic-guida-ndc-docs/).

## Layout e regole del repository

Questa sezione descrive l'alberatura generale di un Repository semantico.

Tutte le risorse semantiche sono nella cartella [assets](assets/),
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

Per approfondire il tema del layout del repository, il contenuto richiesto, 
il versionamento delle risorse, e per poter consultare alcuni esempi utili,
fai riferimento alla
[sezione dedicata nel Manuale Operativo del Catalogo](https://teamdigitale.github.io/dati-semantic-guida-ndc-docs/docs/manuale-operativo/istruzioni-su-come-predisporre-il-repository-in-cui-pubblicare-le-risorse-semantiche.html).


## Controlli Automatici e Test

Questa sezione descrive le procedure di controllo automatico e test, 
utili per garantire la qualità e l'integrità del contenuto del repository.

### Controlli Automatici (Pre-commit)

Questo repository implementa i controlli automatici utilizzando [pre-commit](https://pre-commit.com/). 
Le specifiche delle verifiche sono definite nel file [`.pre-commit-config.yaml`](.pre-commit-config.yaml).

È possibile eseguire tali verifiche mediante GitHub Actions. 
Il file `validate.yaml` in `.github/workflows` abilita automaticamente 
i controlli pre-commit dopo ogni push o pull request (PR). 
Inoltre, è possibile eseguirli manualmente in qualsiasi momento.

Per abilitare i controlli pre-commit in un altro repository, 
copiare il file [`.pre-commit-config.yaml`](.pre-commit-config.yaml) e il file [`.github/workflows/validate.yaml`](.github/workflows/validate.yaml).

Nota: È possibile commentare i controlli ritenuti non necessari o inappropriati. 
Ad esempio, se si utilizza una soluzione con URI stabili, 
il controllo di validazione del nome del file 
rispetto agli URI (`validate-filename-match-uri`) potrebbe non essere indispensabile.

### Test URL

Lo script `test_urls.py` nella directory `tests` consente di verificare 
gli URL relativi a GitHub presenti nei file delle sottodirectory `assets`.

Anche questo test può essere automatizzato mediante GitHub Actions. 
Il file `test.yaml` in `.github/workflows` attiva automaticamente i test 
dopo ogni push o pull request. 
Inoltre, è possibile eseguirli manualmente in qualsiasi momento.

Per abilitare i test URL in un altro repository,
copiare il file [`/tests/test_urls.py`](/tests/test_urls.py) e il file [`.github/workflows/test.yaml`](.github/workflows/test.yaml).

### Controlli e Test in Locale

I controlli e i test possono essere eseguiti anche in locale
con Docker o Python. Usa `docker-compose` per replicare
la pipeline CI:

```bash
docker-compose -f docker-compose-test.yml up
```

Nota: Per trasferire questo ambiente su un altro repository, 
è necessario includere i Dockerfile 
presenti nella directory `tests` (come `Dockerfile.precommit` e `Dockerfile.pytest`).

