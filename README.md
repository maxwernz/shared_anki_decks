# Anki Deck Repo

1. Anki Connect installieren: Den Code von der Anki Connect Internetseite kopieren und in Anki über Extras -> Erweiterungen installieren und neustarten
2. Repo klonen
3. Shebang in 'anki.py' auf euern python Pfad ändern, damit ihr das ganze aus der Kommandozeile (oder Doppelklick?!) starten könnt.
4. 'anki.py' ausführen
5. eventuell `pip install requests` und `pip install GitPython` machen, wenn die nicht installiert sind

**Falls bei euch die Python Files änderungen haben, z.B. durch das ändern des Shebangs, nicht committen, lasst die einfach unstaged**
   

## Import
**Anki muss geöffnet sein**
Alle Decks müssen flach auf der selben Ebene wie das Skript liegen. 
Beim Ausführen des Skripts wird automatisch vom repo gepullt und alle Decks in Anki geladen. 
Dadurch bleibt einem das pullen erspart und man kann zum Aktualisieren einfach immer das Skript ausführen.

## Export
**Anki muss geöffnet sein**
Zum Exportieren von Decks einfach das Export Skript `export_anki.py` ausführen.
Dabei per Kommandozeile den oder die Namen der Decks übergeben( z.B. ./export_anki.py BME).
Das wird dann automatisch in den Ordner exportiert, committet und gepusht.

