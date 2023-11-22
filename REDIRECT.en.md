# Guide to URI redirection

This document provides guidance for creating and publishing
`htaccess` files that allow redirection of semantic resources 
URIs using the w3id.

## Requirements Notation

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT",
"RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL"
in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when,
and only when, they appear in all capitals, as shown here.

## Introduction to redirect

[w3id.org](https://w3id.org/) is a solution from the W3C Permanent Identifier Community Group that allows the addition or modification of permanent identifiers from which to redirect to specific URLs; the process is based on adding one or more folders in the [w3id git repository](https://github.com/perma-id/w3id.org), which MUST contain the `.htaccess` files and `README.md`, possibly organized into subfolders.

In the case of the Catalogue, it is necessary to refer to the [Italy folder of the w3id GIT](https://github.com/perma-id/w3id.org/tree/master/italia), in which the subfolders MUST be added, each for a particular thematic area, which will contain the redirection files, possibly organized in further subfolders, and the `README.md` file. The addition of the `'/Italy'` subfolders will be subject to approval by the Italy Committee; subsequently, they will be managed independently and with direct interfacing between w3id.org and the contacts indicated in the `README.md`. The folder and its subfolders, `.htaccess` files, and `README.md` files MUST be created on the [w3id git repository](https://github.com/perma-id/w3id.org) by the Contributor.

## Publishing htaccess on w3id

### 1. fork of the w3id.org GIT repository

The first step for registering the redirects is the local fork of the
[w3id GIT Italy folder](https://github.com/perma-id/w3id.org/tree/master/italia). The
permanent identifiers (URI) will be defined based on the path in which the various `htaccess` files will be inserted.
In this case, the path to the "root" folder for folder-name must be `"italia/<folder-name>/"`, therefore the namespace of the URIs defined in it will be `w3id.org/italia/<folder-name>/`.

### 2. adding the folder

In the local repository created starting from the fork, it will be necessary to create the `folder-name` folder which will contain the tree of subfolders and the related `.htaccess` files, in addition to the `README.md`.

Below is an example of a folder tree under `"/italia"`:

<pre>
italia
|--folder-name
|   |--controlled-vocabulary
|   |   |-.htaccess
|   |--data
|   |   |-.htaccess
|   |--onto
|   |   |-.htaccess
|   |README.md
</pre>

This will define the following URIs:
-	`w3id.org/italia/<folder-name>/controlled-vocabulary`
-	`w3id.org/italia/<folder-name>/data`
-	`w3id.org/italia/<folder-name>/onto`

The `<folder-name>` is very important as it MUST be placed in specific parameters described later in this document, and will always be used to refer to the Contributor's set of semantic resources as part of the redirect file configuration.

The redirect rules associated with each uri MUST be defined in the relevant `.htaccess` files described below. The `README.md` file MUST contain the names of the contacts along with their email and github references. These references MUST take care of the management of the folder and related files following the approval of "Italia". You SHOULD take the `README.md` file under the `"/italia"` folder as an example.

### 3. creating the pull request

Once the GIT repository has been modified locally, a pull request MUST be created, which will be analyzed and possibly validated by "Italia"; in the pull request the contacts present in the [README.md file under “/italia”](https://github.com/perma-id/w3id.org/blob/master/italia/readme.md) MUST be indicated as reviewers.
The merge on the master branch will be carried out directly from w3id.org and will determine the definitive publication of the new URIs and related redirect rules.

## Contents of htaccess and README.md files

Below is a description of the `.htaccess` file for each type of resource, from which the contributing organization SHOULD take inspiration in order to create its own redirect files.

### controlled-vocabulary

The `.htaccess` file to be inserted in the `“italia/name-folder/controlled-vocabulary”` subfolder SHOULD be created by taking as an example [the one contained in the GIT folder “italia/controlled-vocabulary”](https://github.com/perma-id/w3id.org/blob/master/italia/controlled-vocabulary/.htaccess).

It contains code written based on Apache Directives, and allows you to manage HTTP requests based on the value of the Accept header and SYNTAX. Depending on the value, the URLs are rewritten differently or redirected to external URLs. The specific rewrite or redirect action depends on the combination of Accept and SYNTAX.

Below is a description of the example directives, to which the references of the landing URLs MUST be modified, in addition to any modification/integration of the rules in order to better adapt to the Contributor's git:

<pre>
Header set Access-Control-Allow-Origin *
</pre>
This line sets the Access-Control-Allow-Origin header to *, allowing any domain to access resources on the server via Ajax requests or from other different domains.

<pre>
Options +FollowSymLinks
</pre>
This line enables the FollowSymLinks option, which allows the server to follow symbolic links (symlinks) within the file system.

<pre>
RewriteEngine on
</pre>
This line activates Apache's URL rewriting engine (mod_rewrite), which allows you to manipulate the URLs of HTTP requests.

<pre>
SetEnvIf Accept ^.*text/turtle.* SYNTAX=ttl
SetEnvIf Accept ^.*application/json.* SYNTAX=json
SetEnvIf Accept ^.*application/csv.* SYNTAX=csv
SetEnvIf Accept ^.*text/csv.* SYNTAX=csv
SetEnvIf Accept ^.*text/html.* SYNTAX=html
</pre>
These lines set an environment variable called SYNTAX based on the Accept header of the HTTP request. This is used to determine the type of syntax required in the response. These lines MUST be modified depending on the file formats present in your github folders.

<pre>
SetEnvIf Request_URI ^.*$ ROOT_URL="url-git"
</pre>
Set the ROOT_URL environment variable with a fixed URL. The URL entered MUST be that of your repository pointing to the controlled vocabularies folder (in the format `"https://raw.githubusercontent.com/..."`)

<pre>
RewriteCond %{ENV:SYNTAX} ^(ttl|json|csv)$
RewriteRule ^([a-zA-Z-_0-9]+)(/?)$ %{ENV:ROOT_URL}$1/latest/$1.%{ENV:SYNTAX} [R=303,L]
</pre>
Defines the URL rewriting rule if the requested file type is ttl, json or csv ( types MUST be configured based on the file types present in the source repository).

<pre>
RewriteCond %{ENV:SYNTAX} ^html$
RewriteRule ^(.+)$ https://schema.gov.it/lodview/"nome-cartella"/controlled-vocabulary/$1 [R=303,L]
RewriteRule ^(.+)/(.+)/(.+)$ https://schema.gov.it/lodview/"nome-cartella"/controlled-vocabulary/$1/$2/$3 [R=303,L]
</pre>
The previous conditions apply only when SYNTAX is html, or in all other cases not managed by the previous conditions. They rewrite URLs differently, redirecting to external URLs based on specific patterns. They MUST be configured based on the name of the thematic folder which refers to the particular set of semantic resources in the w3id's git.

### onto

The `.htaccess` file to be inserted in the “italia/foldername/onto” subfolder SHOULD be created starting from [the one contained in the “italia/onto” GIT folder](https://github.com/perma-id/w3id.org/blob/master/italia/controlled-vocabulary/.htaccess)

It contains code written based on Apache Directives, and allows you to manage HTTP requests based on the value of the Accept header and SYNTAX. Depending on the value, the URLs are rewritten differently or redirected to external URLs. The specific rewrite or redirect action depends on the combination of Accept and SYNTAX.

Below is a description of the example directives, to which the landing URL references MUST be modified, in addition to any modification/integration of the rules in order to better adapt to the Contributor's git:

<pre>
Header set Access-Control-Allow-Origin *
</pre>
This line sets the Access-Control-Allow-Origin header to *, allowing any domain to access resources on the server via Ajax requests or from other different domains.

<pre>
Options +FollowSymLinks
</pre>
This line enables the FollowSymLinks option, which allows the server to follow symbolic links (symlinks) within the file system.

<pre>
RewriteEngine on
</pre>
This line activates Apache's URL rewriting engine (mod_rewrite), which allows you to manipulate the URLs of HTTP requests.

<pre>
SetEnvIf Accept ^.*application/rdf\+xml.* SYNTAX=rdf
SetEnvIf Accept ^.*application/rdf\+xml.* SYNTAX=owl
SetEnvIf Accept ^.*application/n-triples.* SYNTAX=n3
SetEnvIf Accept ^.*text/turtle.* SYNTAX=ttl
SetEnvIf Accept ^.*text/html.* SYNTAX=html
</pre>
These lines set an environment variable called SYNTAX based on the Accept header of the HTTP request. This is used to determine the type of syntax required in the response. These lines MUST be modified according to the file formats present in your folders in the semantic resources repository.

<pre>
SetEnvIf Request_URI ^.*$ ROOT_URL="url-git"
</pre>
Set the ROOT_URL environment variable with a fixed URL. The URL entered MUST be that of your repository pointing to the ontologies folder (in the format `"https://raw.githubusercontent.com/..."`)

<pre>
RewriteCond %{ENV:SYNTAX} ^(rdf|ttl|owl|n3)$
RewriteRule ^([a-zA-Z-_0-9]+)(/?)$ %{ENV:ROOT_URL}$1/latest/$1.%{ENV:SYNTAX} [R=303,L]
</pre>
Defines the URL rewriting rule if the requested file type is rdf, ttl, own or n3 (file types MUST be configured based on the file types present in the source repository).

<pre>
RewriteCond %{ENV:SYNTAX} ^html$
RewriteRule ^(.+)(/.+)$ https://schema.gov.it/lodview/"nome-cartella"/onto/$1$2 [R=303,L]
RewriteCond %{ENV:SYNTAX} ^html$
RewriteRule ^(.+)/$ https://schema.gov.it/lode/extract?url=https://w3id.org/italia/"nome-cartella"/onto/$1 [R=303,L]
RewriteCond %{ENV:SYNTAX} ^html$
RewriteRule ^(.+)$ https://schema.gov.it/lode/extract?url=https://w3id.org/italia/"nome-cartella"/onto/$1 [R=303,L]
</pre>
The above conditions apply only when SYNTAX is html. They rewrite URLs differently, redirecting to external URLs based on specific patterns. They MUST be configured based on the name of the thematic folder which refers to the particular set of semantic resources in the w3id's git.

### data

The `.htaccess` file to be inserted in the “italia/folder-name/data” subfolder SHOULD be created starting from [the one contained in the “italia/data” GIT folder](https://github.com/perma-id/w3id.org/blob/master/italia/data/.htaccess).

It contains code written based on the Apache Directives, and allows you to configure the Apache server to allow access from any domain to the server's resources, set a ROOT_URL environment variable with a fixed value, and then rewrite all requests so that include ROOT_URL before the requested URI.

Below is a description of the example directives, to which the landing URL references MUST be modified, in addition to any modification/integration of the rules in order to better adapt to the Contributor's git:

<pre>
Header set Access-Control-Allow-Origin *
</pre>
This line sets the Access-Control-Allow-Origin header to *, allowing any domain to access resources on the server via Ajax requests or from other different domains.

<pre>
Options +FollowSymLinks
</pre>
Questa riga abilita l'opzione FollowSymLinks, che permette al server di seguire i collegamenti simbolici (symlink) all'interno del file system.

<pre>
RewriteEngine on
</pre>
This line enables the FollowSymLinks option, which allows the server to follow symbolic links (symlinks) within the file system.

<pre>
SetEnvIf Request_URI ^.*$ ROOT_URL=https://schema.gov.it/lodview/"nome-cartella"/data/
</pre>
This line sets an environment variable called ROOT_URL, which MUST be changed based on the subject folder name
which refers to your semantic resource repository on w3id.

<pre>
RewriteRule ^(.*)$ %{ENV:ROOT_URL}$1 [R=303,L]
</pre>
This line is a URL rewrite rule. Every request that comes to the server will be rewritten to include the value of ROOT_URL before the requested URI. The [R=303,L] flag indicates that the HTTP response will be a temporary redirect (status code 303) and that this is the last rule to be applied.

<pre>
RewriteRule ^(.*)/$ %{ENV:ROOT_URL}$1 [R=303,L]
</pre>
This is a similar rewrite rule to the previous one, but only applies to requests that end with a slash. Again, the response will be a temporary redirect with status code 303.

### README.md

To create the README.md file you MAY refer to the [example provided by w3id.org itself](https://github.com/perma-id/w3id.org/blob/master/dggs/README.md) , or to the [file created under the “/italia” folder](https://github.com/perma-id/w3id.org/blob/master/italia/readme.md).

In any case, you MUST describe the purpose of the URIs and insert the names of the contact persons in the "contacts" section.