# Risorse semantiche per il National Data Catalog

Questo documento definisce le linee guida per pubblicare sul
National Data Catalog for Semantic Interoperability - di seguito NDC - usando un
repository git.

## Terminologia

Conformemente alle norme ISO/IEC Directives, Part 3 per la stesura dei documenti tecnici
questo documento utilizza le parole chiave "DEVE", "DEVONO", "NON DEVE", "NON DEVONO", "DOVREBBE",
"NON DOVREBBE", "PUÒ" e "OPZIONALE", la cui interpretazione è descritta di seguito.

- DEVE o DEVONO, indicano un requisito obbligatorio per rispettare le Linee Guida;
- NON DEVE o NON DEVONO, indicano un assoluto divieto delle specifiche;
- DOVREBBE o NON DOVREBBE, indicano che le implicazioni devono essere comprese
  e attentamente pesate prima di scegliere approcci alternativi;
- PUÒ o POSSONO o l’aggettivo OPZIONALE, indica che il lettore può scegliere
  di applicare o meno senza alcun tipo di implicazione o restrizione la specifica

## Contenuto del repository

Ogni repository può contenere una o più risorse  semantiche.
Quelle supportate sono:

- Ontologie;
- Vocabolari controllati (e.g., tassonomie, code list, tesauri);
- Schemi dati in formato OAS3 (OpenAPI Specifications versione 3).

Future versioni del NDC possono supportare altre risorse semantiche
ed altri formati.

## File richiesti e layout del repository

Il repository DEVE contenere i seguenti file:

- ndc-config.yaml: referenziando la posizione delle risorse semantiche
  ed ulteriori informazioni necessarie
  alla pubblicazione su NDC;
- publiccode.yaml: contenente tutte le informazioni richieste dal
  [Catalogo del Riuso](https://developers.italia.it/it/software).

Un repository è a tutti gli effetti un oggetto pubblico indicizzato dal Catalogo del Riuso,
e DEVE contenere un file [publiccode.yml conforme alle relative Linee Guida](https://docs.italia.it/italia/developers-italia/publiccodeyml)
col riferimento al [codice IPA](https://www.indicepa.gov.it/) dell'ente che gestisce il repository.

Queste informazioni verranno utilizzate anche per la continuità operativa del NDC.

```yaml
...
maintenance:
  contacts:
email: info@teamdigitale.governo.it
name: Dipartimento per la Trasformazione Digitale
it:
  riuso:
    codiceIPA: pcm
```

Tutte le risorse fornite DEVONO risiedere all'interno della cartella `assets/`
referenziato in ndc-config.yaml.
Le risorse al di fuori di `assets/` non saranno elaborate.

Ogni tipo di asset (ontologie, vocabolari controllati, schemi)
DEVE risiedere nella sua cartella specifica con un nome predefinito,
referenziato in ndc-config.yaml.

I nomi di file e directory DEVONO corrispondere
al pattern `[A-ZA-Z0-9 _-.]{, 64}`.
Gli spazi NON DEVONO essere utilizzati nei file o nei nomi delle directory.
Le directory DEVONO essere in minuscolo.

Il nome di ciascun file DEVE corrispondere al nome della relativa risorsa 
nell'URI utilizzato per referenziarla. 
I nomi dei file di una directory DEVONO corrispondere al nome della directory
che li contiene, a meno dell'estensione degli stessi.

Inoltre, DEVONO essere creati e pubblicati sul repository del w3id i file
`htaccess` che definiscono le regole di redirect delle URI, così come descritto
 in [REDIRECT.md](REDIRECT.md).

I contenuti degli asset DEVONO essere codificati in UTF-8 o ASCII.

Ogni risorsa DEVE risiedere sotto la sua cartella specifica:

- ontologies: in `assets/ontologies/`;
- Vocabolari controllati: in `assets/controlled-vocabularies/`;
- Schemi: in `assets/schemas/`.

Ad esempio, il percorso di `MyOntology` sarà `assets/ontologies/MyOntology/`.

### File di documentazione

Le directory degli asset POSSONO contenere
file di documentazione in formato Markdown.
L'estensione del file DEVE essere `.md` (ad esempio `README.md`).
Questi file non saranno elaborati.

### Directory versionate

Le directory degli asset POSSONO essere strutturate con ulteriori sub-directory
per supportare il versionamento. Il nome delle sub-directory DEVE corrispondere al
pattern: `(latest|v?[0-9]+(\.[0-9]+){0,2})`.
Una cartella per gli asset NON DEVE contenere contemporaneamente sub-directory
versionate con e senza il prefisso `v`.

Tre esempi di nomi validi di sub-directory:

```
assets/ontologies/CPV/v0.4.2/
assets/ontologies/CPV/0.5/
assets/schemas/Person/latest/
```

Il Catalogo elabora solo:

- la cartella `latest` se presente;
- La cartella con l'ultima versione,
  secondo la sintassi indicata dal semantic versioning.

### Nessuna rappresentazione RDF alternativa

Le directory degli asset NON DEVONO contenere
risorse RDF in altre serializzazioni
(ad es. RDF / XML, JSON-LD, ..).
Queste non saranno elaborate.

Questi file POSSONO essere inseriti nello stesso
repository al di fuori della cartella `assets/`;
In questo caso, essi
DOVREBBERO essere generati automaticamente
dai file originali in `assets/`.

## Ontologie

Le ontologie pubblicate DEVONO essere conformi alle relative
Linee guida nazionali.

Le ontologie DEVONO essere pubblicate solo in formato RDF/Turtle
(media-type `text/turtle`) e l'estensione del file DEVE essere `.ttl`.

## Vocabolari controllati

I vocabolari controllati pubblicati DEVONO essere conformi alle relative
Linee guida nazionali.

I vocabolari controllati DEVONO essere pubblicati solo in formato RDF/Turtle
(media-type `text/turtle`) e l'estensione del file DEVE essere `.ttl`.

Le directory del vocabolario controllate DOVREBBERO contenere
una proiezioni in formato CSV del vocabolario
insieme ai metadati necessari per mappare i campi del CSV
alle risorse presenti nell'RDF:
Questa proiezione in formato CSV sarà esposta dalla NDC tramite API REST.
L'estensione del file DEVE essere `.csv`.

I metadati di cui sopra DEVONO essere espressi
tramite un `@context` [JSON-LD 1.1](https://www.w3.org/TR/json-ld11/).

## Schemi

Gli schemi pubblicati devono essere conformi alle relative Linee guida nazionali.

Gli schemi per le API dell'OAS3 devono essere pubblicati in formato OpenAPI3,
Incorporato nella sezione `#/components/schema` del file OAS.
L'estensione del file DEVE essere `.oas3.yaml`.

In futuro potranno essere supportati altri tipi di schemi.

Il file YAML DOVREBBE contenere i riferimenti semantici attraverso
il campo custom `x-jsonld-context` conforme alle indicazioni
contenute in [JSON-LD 1.1](https://www.w3.org/TR/json-ld11/).

Un esempio di file OAS3 metadatato con il campo `x-jsonld-context`:

```yaml
openapi: 3.0.1
...
components:
  schemas:
    Person:
      type: object
      x-jsonld-context:
        "@vocab": "https://w3id.org/italia/onto/CPV/"
        nome_proprio: givenName
        cognome: familyName
      properties:
        nome_proprio: {type: string, ..}
        cognome: {type: string, ..}
      ...

```

I metadati associati DEVONO essere pubblicati solo in formato RDF/Turtle
(media-type `text/turtle`) e l'estensione del file DEVE essere `.ttl`.
Questo file DOVREBBE essere generato automaticamente
dal file YAML.

Gli schemi forniti POSSONO essere verificati sintatticamente utilizzando
l'[OpenAPI Checker](https://italia.github.io/api-oas-checker).

## Controlli automatici

Il repository DOVREBBE utilizzare strumenti di continuous integration
come github-actions o gitlab-ci per verificare la consistenza dei contenuti.
