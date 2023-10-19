# Anki Deck Repo

1. Anki Connect installieren: Den Code von der Anki Connect Internetseite kopieren und in Anki über Extras -> Erweiterungen installieren und neustarten
2. Repo klonen
3. Shebang in 'anki.py' auf euern python Pfad ändern, damit ihr das ganze aus der Kommandozeile (oder Doppelklick?!) starten könnt.
4. 'anki.py' ausführen
5. eventuell `pip install requests` und `pip install GitPython` machen, wenn die nicht installiert sind
   

## Funktion
Alle Decks müssen flach auf der selben Ebene wie das Skript liegen. 
Beim Ausführen des scripts wird automatisch vom repo gepullt und alle Decks in Anki geladen. 
Dadurch bleibt einem bisschen das pullen erspart und man kann zum Aktualisieren einfach immer das Skript ausführen.
Um neue Sachen zu pushen einfach das Deck aus Anki heraus in den Ordner vom Repo mit allen anderen Decks exportieren und das alte überschreiben, dann ganz normal committen und pushen.


