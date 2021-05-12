## Github Actions CI
1. Workflow megismerése, konfigurálása
    - Actions működésének megismerése, előre elkészített modulok keresése
    - Workflow leírása egy yaml file-ban könnyen megtehető, egyszerű követni a működést
    - Elsőként a futtatást kell beállítani a megfelelő branchekre és PR esetén
    - Ezután a megfelelő modulokat beállítani a checkoutra, ubuntu vm indítására, Python telepítésére
    - A környezet felépítése után már könnyen telepíthetők a szükséges Python package-ek és futtathatók a tesztek
2. Idő közben bejött tesztmodul (behave) hozzáadása
    - A package a függőségekből automatikusan települ
    - Minden BDD teszt futtatására csupán ki kell adni a `behave` parancsot
3. Kódlefedettség hozzáadásának átvizsgálása
    - Codecov megismerése
    - Kevés konfigurációval már át is tudja vizsgálni a repót és a workflow-hoz is könnyen hozzáadható

Összességében úgy vélem a létrehozott CI megoldás biztosítja az általunk létrehozott tesztek futtatását és a folytonos integrációhoz szükséges ellenőrzéseket. Emellett a projekt tesztlefedettségének vizsgálatát is vártan végzi.
