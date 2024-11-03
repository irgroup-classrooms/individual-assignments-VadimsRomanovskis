# Data Modelling Project (Winter 2024/25)

## To-Do List for the Semester
Here are some topics I've heard about and would like to learn throughout the semester.

- [ ] **Dataset Selection**: Choosing appropriate datasets and understanding their structure.
- [ ] **Data Cleaning and Preparation**: Cleaning, handling missing values, and formatting data.
- [ ] **Data Analysis**: Using Python and Pandas for data manipulation and exploratory analysis.
- [ ] **Data Visualization**: Creating meaningful visualizations to support findings.
- [ ] **Web Scraping**: Enhancing datasets by scraping additional data.
- [ ] **Documentation**: Keeping clear and structured documentation for the project.
- [ ] **Version Control**: Managing files and collaborating with Git and GitHub.

---

### Markdown Syntax Cheat Sheet

| Element                     | Syntax                               | Example                                   |
|-----------------------------|--------------------------------------|-------------------------------------------|
| **Heading**                 | `# Heading 1`                       | # Heading 1                               |
| **Bold Text**               | `**bold text**`                     | **bold text**                             |
| **Italic Text**             | `*italicized text*`                 | *italicized text*                         |
| **Strikethrough**           | `~~strikethrough~~`                 | ~~strikethrough~~                         |
| **Underline**               | `<u>underline</u>`                  | <u>underline</u>                          |
| **Bold and Italic**         | `***bold and italic***`             | ***bold and italic***                     |
| **Superscript**             | `text<sup>superscript</sup>`        | text<sup>superscript</sup>                |
| **Subscript**               | `text<sub>subscript</sub>`          | text<sub>subscript</sub>                  |
| **Quote**                   | `> This is a quote`                 | > This is a quote                         |
| **Ordered List**            | `1. Item 1`                         | 1. Item 1                                 |
| **Unordered List**          | `- Item`                            | - Item                                    |
| **Link**                    | `[text](URL)`                       | [Google](https://www.google.com)          |
| **Image**                   | `![alt text](image.jpg)`            | ![Logo](https://upload.wikimedia.org/wikipedia/commons/0/0e/TH_Koeln_Logo.svg) |
| **Inline Code**             | `` `inline code` ``                 | `inline code`                             |
| **Code Block**              | \`\`\` code here \`\`\`             | ```print("Hello World!")```               |
| **Table**                   | `| col 1 | col 2 |`                 | \| col 1 \| col 2 \|                      |
| **Checkbox**                | `- [ ] unchecked`                   | - [ ] Task                                |
| **Horizontal Line**         | `---` or `***`                      | ---                                       |
| **Emojis**                  | `:smile:`                           | 😄                                       |
| **Highlight Text**          | `==highlight==`                     | ==highlight==                             |
| **Escape Character**        | `\*escaped asterisk\*`              | \*escaped asterisk\*                      |
| **Footnote**                | `[^1]` and `[^1]: footnote text`    | [^1]                                      |
| **HTML Tags**               | `<br>`, `<hr>`, `<mark>highlight`   | `<mark>highlight</mark>`                  |

---

**Notes:**
- Superscript and subscript require HTML tags in Markdown.
- Emojis are added with `:` and the emoji name.
- Highlight text might not work on all platforms.


## Inspirational Quote
> *"Tu was du kannst, mit dem was du hast, und dort wo du bist."*

---

## Code Snippet
This code represents a simple game of ‘Hangman’ that I wrote in the ***"Programming and Software Entwicklung"*** course in Technische Hochschule Köln:

```python
import random

# Eine Liste von Wörtern zur Auswahl für das Spiel
Woerter = 'Abend Abschnitt Abstimmung Abteilung Aktion Aktivität Anbieter Angriff Angst Betrieb Anlass Anschlag Ansicht Anstieg Anzeige Arbeitsplatz Arbeitsschritt Artikel Aufklärung Aufmerksamkeit Aufnahme Auge Ausbildung Ausdruck Auskunft Ausland Auto Bahn Band Bank Beispiel Beratung Berufung Betrag Bewegung Bewertung Bezeichnung Bier Boden Branche Brief Buch Bühne Bund Bundesliga Bundesrepublik Bündnis Büro Dach Dank Darstellung Demokratie Dokumentation Dorf Drittel Ecke Einkommen Einsatz Einstellung Engagement Erinnerung Erklärung Essen Euro Farbe Fehler Feld Fest Feuer Figur Finanzierung Fläche Forderung Fortsetzung Foto Fraktion Frieden Fünf Fusion Fuß Galerie Gebäude Geburtstag Gefängnis Gegensatz Gegenteil Geist Gelände Genehmigung Gewinn Glück Grenze Größe Gutachten Hälfte Haushalt Hintergrund Hinweis Hof Hotel Idee Image Industrie Inhalt Institut Integration Internet Katastrophe Keller Kennzeichen Kern Kilogramm Kollege Konferenz König Konkurrenz Kontakt Konzept Konzern Konzert Körper Kraft Krankenhaus Krankheit Krieg Kritik Kultur Kunst Landkreis Landtag Landwirtschaft Leistung Leitung Liebe Liter Lösung Material Mehrheit Meinung Menge Methode Mischung Mitte Mittel Mittelpunkt Möglichkeit Moment Mord Morgen Nachfrage Nachmittag Nachricht Nacht Nase Netz Niederlage Niveau Objekt Oper Patient Pflanze Phase Post Posten Premiere Prinzip Protest Punkt Quadratmeter Qualität Rang Rathaus Realität Rechnung Recht Regen Reise Rennen Revolution Roman Rückgang Rückkehr Ruhe Saal Sache Saison Sammlung Sanierung Schloss Schlüssel Schreiben Schwerpunkt Senat Sender Serie Service Sicht Sitzung Sommer Sorge Spaß Spielen Spitze Staat Steigerung Stelle Steuer Stimmung Stoff Straße Strecke Stück Studium Summe Tatsache Technik Insel Teilnahme Tendenz Tier Tod Tonne Treffen Trend Trennung Überlegung Umsatz Umsetzung Universität Unterschied Unterstützung Untersuchung Urlaub Ursache Urteil Variante Veranstaltung Verband Verbesserung Verbrechen Verdacht Vereinbarung Verfügung Vergleich Verhältnis Version Verteidigung Verwaltung Voraussetzung Vorbereitung Vorgang Vorgehen Vorhaben Vorlage Vorstellung Wagen Wahrheit Welt Wert Wetter Widerstand Wirklichkeit Wirkung Wissenschaft Wohnung Wunder Zeitpunkt Zeitschrift Zeitung Zins Zugang Zweifel'.split()

# Wähle ein zufälliges Wort aus der Liste
Wort = random.choice(Woerter)
Erraten = []                     # Liste zur Speicherung der erratenen Buchstaben
Versuche = 9                     # Anzahl der erlaubten Fehlversuche
verwendete_buchstaben = []       # Liste zur Speicherung bereits verwendeter Buchstaben

# Initialisierung: Platzhalter "_" für jeden Buchstaben im Wort
for Buchstaben in Wort:
    Erraten.append('_')

# Hauptspielschleife
while True:
    # Ausgabe des aktuellen Fortschritts
    for Ausgabe in Erraten:
        print(Ausgabe, end=' ')
    print()
    
    # Nutzereingabe für den nächsten Buchstaben
    Nutzereingabe = input("Ihr Vorschlag:")
    
    # Überprüfung, ob der Buchstabe bereits verwendet wurde
    if Nutzereingabe.lower() in verwendete_buchstaben:
        print("Dieser Buchstabe wurde bereits verwendet. Bitte versuchen Sie es erneut.")
        continue

    # Suche nach dem Buchstaben im Wort
    x = 0
    buchstabe_gefunden = False
    for Buchstaben in Wort:
        if Buchstaben.lower() == Nutzereingabe.lower():
            print("Treffer")
            Erraten[x] = Buchstaben
            buchstabe_gefunden = True
        x += 1
    print()

    # Füge den Buchstaben zur Liste der verwendeten Buchstaben hinzu, falls er gefunden wurde
    if buchstabe_gefunden:
        verwendete_buchstaben.append(Nutzereingabe.lower())

    # Überprüfung, ob das Wort vollständig erraten wurde
    if '_' in Erraten:
        # Verringern der verbleibenden Versuche, falls der Buchstabe nicht im Wort ist
        if Nutzereingabe.lower() not in Wort.lower():
            Versuche -= 1
        print("Verbleibende Versuche: ", Versuche)

        # Spielende, falls keine Versuche mehr übrig sind
        if Versuche == 0:
            print("Schade, Sie haben verloren! Das Wort war:", Wort)
            break
        
        # Spielende, falls das Wort vollständig erraten wurde
        if Nutzereingabe.lower() == Wort.lower():
            print("Super! Sie haben das Wort erraten!")
            break
    else:
        print("Gewonnen!")
        break
