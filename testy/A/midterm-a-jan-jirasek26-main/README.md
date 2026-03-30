[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/nI-TSb-Y)
# Půlsemestrální test 2025/2026 - varianta A


### Klonování a nastavení repozitáře v PyCharmu
1. V PyCharmu vyber možnost <kbd>Pycharm</kbd> → <kbd>Open...</kbd>.
    
    Ve vyskakovacím okně nastav cestu na vytvořenou složku pro půlsemestrální test:

    `C:\Users\xxxxxx\Desktop\prg_midterm`
    
    → <kbd>Select Folder</kbd> → <kbd>This Window</kbd> → <kbd>Trust Project</kbd>
2. Otevři Terminál (<kbd>Alt</kbd> + <kbd>F12</kbd>).
3. V příkazové řádce přejdi do této složky:
    ```commandline
    cd C:\Users\xxxxxx\Desktop\prg_midterm
    ```
4. Naklonuj repozitář s testem:
    ```commandline
    git clone https://path.to.git.repository
    ```
5. V PyCharmu otevři naklonovaný repozitář:

    <kbd>Pycharm</kbd> → <kbd>File</kbd> → <kbd>Open...</kbd>

    Ve vyskakovacím okně nastav cestu na hlavní adresář s půlsemestrálním testem: 

    `C:\Users\xxxxxx\Desktop\prg_midterm\midterm-test-xxx`

    → <kbd>Select Folder</kbd> → <kbd>This Window</kbd> → <kbd>Trust Project</kbd>
6. Vytvoř virtuální prostředí přes Terminál:
    ```commandline
    uv sync
    ```

---

# Ovládání motorizovaného stolku mikroskopu

Cílem je vytvořit program v souboru `microscope_stage.py`, který bude ovládat motorizovaný stolek mikroskopu — zařízení,
které umožňuje přesný pohyb vzorku pod objektivem ve třech osách (*x*, *y*, *z*).

V praxi se takový stolek používá v laboratorních mikroskopech pro automatické skenování biologických vzorků 
(např. tkáňových řezů), kde mikroskop systematicky projede celou plochu preparátu a pořídí na každé pozici snímek. 
Tyto snímky se pak složí do jednoho velkého obrázku s vysokým rozlišením.

Důležité je, aby stolek nepřekročil své fyzické limity (rozsah os) — jinak hrozí mechanické poškození. Proto je nutné 
každou pozici před nastavením zkontrolovat a případně opravit na povolený rozsah.

### Simulace nastavení pozice

Skutečný hardware tu není, proto je v samostatném souboru `stage_simulator.py` připravená
funkce `set_position(x, y, z)`. Ta simuluje HW ovladač stolku tak, že vypíše nastavenou
pozici na obrazovku.

Použití:

```python
from stage_simulator import set_position

set_position(100, -200, 1000)
```
Výstup:

```text
Stage position set to: x=100, y=-200, z=1000
```

### Konfigurace stolku

Konfigurace stolku je uložena v JSON souboru (viz `data/stage_config.json`):

```json
{"x": {"min": -5000, "max": 5000}, "y": {"min": -3000, "max": 3000}, "z": {"min": 0, "max": 2000}}
```

### Příkazy pro stolek

Pozice jsou uloženy v CSV souboru s hlavičkou `x,y,z` (viz `data/commands_0.csv`):

```
x,y,z
500,0,1000
500,-200,1000
500,-200,1100
```

Každý řádek obsahuje cílovou absolutní pozici stolku ve všech třech osách (`x`, `y`, `z`).

### Pozice

Pozice stolku je reprezentována slovníkem:

```python
position_example = {'x': 100, 'y': -200, 'z': 1000}
```

V tomto zadání budeme všechny pozice reprezentovat jako celá čísla (`int`).
Všechny výpočty i hodnoty zapisované do návratových hodnot a CSV tedy mají být celočíselné.

### Předpoklady pro řešení

V testech můžeš předpokládat, že:

* vstupní JSON i CSV soubory mají správný formát,
* osa v CSV je vždy jedna z hodnot `x`, `y`, `z`,
* pozice vždy obsahuje všechny tři osy `x`, `y`, `z`,
* všechny hodnoty pozic v CSV i konfiguraci jsou celá čísla,
* kroky `step_x` a `step_y` jsou kladná celá čísla,
* konfigurace v testech je zvolená tak, aby i domácí pozice vyšla jako celé číslo.

---

## Úkol 1 – načtení konfigurace

Konfigurace stolku je uložená v externím JSON souboru, protože fyzické limity zařízení se
mohou lišit podle konkrétního přístroje. Cílem této funkce je proto jednoduše otevřít
zadaný soubor a vrátit jeho obsah jako slovník.

* Vytvoř funkci `read_stage_config()`.

* Funkce bude mít jeden vstupní parametr:
    * cesta k souboru (str).

* Funkce bude vracet jednu hodnotu:
    * konfigurace stolku (dict) — viz ukázka výše.

---

## Úkol 2 – domácí pozice

Po spuštění mikroskopu dává smysl přesunout stolek do výchozí neutrální polohy, tedy do
středu jeho mechanického rozsahu. Tato funkce má pro každou osu spočítat aritmetický průměr
hodnot `min` a `max` z konfigurace a vrátit výslednou domácí pozici jako slovník se stejnými
klíči `x`, `y`, `z`. Funkce jen počítá hodnoty, nic nenastavuje a nepracuje se soubory.

Vzorec: $\text{home} = \frac{min + max}{2}$

Domácí pozici vracej také celočíselně (`int`), ne jako `float`.

* Vytvoř funkci `get_home_position()`.

* Funkce bude mít jeden vstupní parametr:
    * konfigurace stolku (dict).

* Funkce bude vracet jednu hodnotu:
    * domácí pozice (dict), např. `{'x': 0, 'y': 0, 'z': 1000}`.

---

## Úkol 3 – bezpečné nastavení pozice

Tato funkce má zajistit, aby se stolek nikdy nepokusil jet mimo svůj povolený rozsah,
protože takový pohyb by mohl poškodit zařízení. Pro každou osu tedy porovnej požadovanou
hodnotu s mezemi z konfigurace, případně ji ořízni na `min` nebo `max`, a teprve potom
zavolej `set_position()`. Vrácená hodnota má odpovídat skutečně nastavené pozici po oříznutí,
aby bylo jasné, kde stolek opravdu skončil.

* Vytvoř funkci `set_position_safe()`.

* Funkce bude mít dva vstupní parametry:
    * požadovaná pozice (dict),
    * konfigurace stolku (dict).

* Funkce bude vracet jednu hodnotu:
    * skutečně nastavená pozice po oříznutí (dict).

---

## Úkol 4 – vykonání příkazů ze souboru

V praxi se pohyby stolku často připraví dopředu do souboru a pak se jen postupně přehrají,
aby byl experiment snadno opakovatelný. Tato funkce má načíst CSV soubor řádek po řádku,
každý řádek převést na cílovou pozici a tu bezpečně vykonat pomocí `set_position_safe()`.
Vrácená hodnota má být seznam všech skutečně nastavených pozic v pořadí, v jakém byly
provedeny. 

* Vytvoř funkci `execute_file()`.

* Funkce bude mít dva vstupní parametry:
    * cesta k CSV souboru s pozicemi (str),
    * konfigurace stolku (dict).

* Funkce bude vracet jednu hodnotu:
    * seznam všech skutečně nastavených pozic (list of dict).

CSV soubor má být ve formátu `x,y,z`, kde každý řádek určuje absolutní cílovou pozici.

---

## Úkol 5 – plán skenování

Při skenování preparátu je potřeba systematicky pokrýt celý pracovní prostor v osách `x` a `y`, typicky po řádcích jako
při čtení mřížky. Pro generování pozic použij vnější smyčku pro postup po ose `y` a vnitřní po ose `x`. Začínáš vždy 
na minimu, přičítáš zadaný krok a bod zapíšeš do souboru jen tehdy, když je ještě v povoleném rozsahu, tedy včetně 
hodnoty přesně rovné maximu. Osa `z` je na všech pozicích stejná a odpovídá domácí poloze, protože skenování probíhá 
v jedné rovině.

Příklad: pro rozsah `0 .. 10` a krok `5` vznikne posloupnost `0, 5, 10` (tři body).

Tato funkce má tedy vygenerovat všechny pozice rastrového skenu a zapsat je do textového souboru ve formátu *x*,*y*,*z*, 
aby je bylo možné později spustit přes `execute_file()`. Do souboru je tedy nutné nejprve zapsat hlavičku `x,y,z` 
a na každém dalším řádku jednu absolutní pozici stolku. Protože v tomto zadání pracujeme jen s celočíselnými pozicemi, 
zapisuj do CSV vždy celá čísla, například `0`, `-5000`, `3000`, `1000`.

* Vytvoř funkci `plan_grid_scan()`.

* Funkce bude mít čtyři vstupní parametry:
    * konfigurace stolku (dict),
    * krok v ose x (int),
    * krok v ose y (int),
    * cesta k výstupnímu souboru (str).

* Funkce bude vracet jednu hodnotu:
    * počet naplánovaných pozic (int).

---

## Úkol 6 – hlavní funkce

Tato funkce představuje jednoduchý hlavní scénář použití celého programu: načte konfiguraci, přesune stolek do domácí
pozice, naplánuje jednoduchý grid scan do souboru, tento soubor vykoná a vypíše, kolik pozic bylo naplánováno. 

Hlavní funkce tedy už nečte žádný hotový soubor s příkazy, ale sama si plán nejdřív vytvoří a pak spustí.
Výpis trajektorie vzniká automaticky při volání `set_position()`, takže v `main()` sám vypisuješ jen
závěrečný souhrnný řádek.

* Vytvoř funkci `main()`.

* Funkce bude mít dva vstupní parametry:
    * cesta ke konfiguračnímu souboru (str),
    * cesta k souboru, do kterého se uloží naplánovaný grid scan a který se potom vykoná (str).

* Funkce nebude vracet žádnou hodnotu.

> Pro jednoduchost použij v `main()` pevný krok skenování `1000` µm v ose `x` i `y`.

Postup má být následující:

1. Načti konfiguraci pomocí `read_stage_config()`.
2. Spočítej domácí pozici pomocí `get_home_position` a nastav ji pomocí `set_position_safe()`.
3. Naplánuj grid scan pomocí `plan_grid_scan()` do souboru zadaného druhým vstupním parametrem funkce `main()`.
4. Spusť tento vygenerovaný soubor pomocí `execute_file()`.
5. Vypiš počet naplánovaných pozic.

### Přesný formát výpisu

```text
Stage position set to: x=<x>, y=<y>, z=<z>
Stage position set to: x=<x>, y=<y>, z=<z>
...
Stage position set to: x=<x grid>, y=<y grid>, z=<z grid>
...
Počet naplánovaných pozic pro grid scan: <počet>
```

Například pro vstupy `data/stage_config.json` a `data/planned_grid_scan.csv` a krok
skenování `1000` v obou osách se nejdřív vykoná domácí pozice, potom všech 77 pozic
uložených v naplánovaném grid scanu a nakonec souhrnný řádek:

```text
Stage position set to: x=0, y=0, z=1000
Stage position set to: x=-5000, y=-3000, z=1000
...
Stage position set to: x=5000, y=3000, z=1000
Počet naplánovaných pozic pro grid scan: 77
```

---

### Příkazy pro git
1. Přidat soubor:
   ```commandline
   git add microscope_stage.py
   ```
2. Vytvořit commit:
   ```commandline
   git commit -m "Commit message"
   ```
3. Odeslat na GitHub:
   ```commandline
   git push origin main
   ```

### Příkazy pro pytest
* Instalace:
  ```commandline
  uv sync
  ```
* Spuštění všech testů:
  ```commandline
  uv run pytest -v
  ```
* Spuštění konkrétního souboru s testy:
  ```commandline
  uv run pytest tests/name_of_the_test_file.py
  ```
