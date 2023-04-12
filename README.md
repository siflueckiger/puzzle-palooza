<h1 align=center>
    <a href="https://puzzle-palooza.netlify.app/">puzzle-palooza.netlify.app</a>
</h1>

Dokumentation des TG53-X für die Präsentation am 6. Mai 2023 am Open Education Day in Bern.

Die Webseite wurde mit dem Static Site Generator [hugo](https://gohugo.io) erstellt.

Als Theme wurde [PaperMod](https://github.com/adityatelange/hugo-PaperMod) für hugo verwendet.

Das Projekt wird auf github geladen und von dort direkt mit [netlify.com](https://www.netlify.com/) ins Netz gestellt.


## 1. Installation
1. Hugo installieren und Repository klonen
   - `brew install hugo`
   - `git clone https://github.com/siflueckiger/puzzle-palooza.git`

## 2. Neuer Beitrag erstellen
Um einen neuen Beitrag zu erstellen im Terminal den Projektordner öffnen.

`cd puzzle-palooza`

Mit folgendem Befehl kann ein neuer Beitrag erstellt werden, in welchen automatisch das Frontmatter-Template eingefügt.

`hugo new dokumentation/<name>.md`

Der neue Beitrag wird mit diesem Befehl im Ordner `Dokumentation` hinzugefügt.

### Frontmatter
Folgende Felder können im Frontmatter angepasst werden.

```yaml
title: "{{ replace .Name "-" " " | title }}"
weight: 1
draft: false
ShowReadingTime: true
showToc: true
tocOpen: false
```

| Name               | Typ     | Beschreibung|
|--------------------|---------|-------------|
| title              | string  | Der Titel des Beitrags. Wird an die Seite des Beitrags als h1-Element weitergegeben.    |
| weight             | integer | Seitenreihenfolge festlegen (1 zu oberst, 99 zu unterst)                                |
| draft              | boolean | `false` (default) Beitrag wird publiziert                                               |
| ShowReadingTime    | boolean | `true` (default) Lesedauer auf Beitragsseite unter Titel anzeigen.                      |
| showToc            | boolean | `true` (default) Ein Inhaltsverzeichnis wird auf der Beitragsseite angezeigt.           |
| tocOpen            | boolean | `false` (default) Inhaltsverzeichnis standardmässig zusammengeklappt.                   |

## 3. Lokal test
Um die Webseite lokal zu testen im Terminal den Projektordner öffnen.

`cd puzzle-palooza`

Mit folgendem Befehl kann die Webseite lokal gehostet werden.

`hugo server`

Lokale Webseite unter dem URL http://localhost:1313/ (ev. auch anderer Port. Steht im Terminal) im Browser aufrufen.

## 4. Webseite publizieren
Die Änderungen in den Branch main auf github pushen.

```sh
git add .
git commit -m "<commit message>"
git push
```

Netlify aktualisiert die Webseite automatisch. So ca. 1-2 Minuten nach dem push sollten die Änderungen auf [puzzle-palooza.netlify.app](https://puzzle-palooza.netlify.app/) ersichtlich sein.

## Noch zu machen
- Eine Seite für Bilder vom TG53-1 erstellen und publizieren.
