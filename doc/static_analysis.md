# Statikus kódanalízis

A statikus analízist a gyakorlaton megismert SonarLint eszköz segítségével végeztük el. A SonarLint eszköz számos hibát és code smell-t jelzett, ezek közül párat javítottunk.
Voltak olyan kódrészletek is, ahol a SonarLint hibásan jelzett, mert valójában nem volt hiba, ilyen esett legtöbbször a teszteknél fordult elő.

## Előforduló hibák típusa:
- Túl hosszú/komplex függvény
- Kikommentezett kód részlet
- Nem használt lokális változó
- Tagváltozó nem jól van elnevezve (pl osztálynévvel van ellátva)
- beégetett stringek 
- Beépített függvény nevével megegyező elnevezés változóknál és függvényeknél (árnyékolás/shadowing)
- exception dobás utáni return


