### Ključne funkcionalnosti

* Ustvarjanje novega kripto portfelja
* Dodajanje nove kriptovalute v kripto portfelj
* Odstranjevanje kriptovalute iz kripto portfelja
* Izračun skupne vrednosti kripto portfelja
* Ogled zgodovine kripto portfelja
* Nastavljanje opozoril
* Izvoz kripto portfelja
* Uvoz kripto portfelja

### Namestitev in zagon

Za namestitev in uporabo aplikacije Crypto Portfolio je potrebno imeti nameščeno Python 3.6 ali novejšo različico. Aplikacijo lahko namestite z naslednjim ukazom:

```
poetry install
```

Za zagon aplikacije uporabite naslednji ukaz:

```
poetry run streamlit run app.py
```

Aplikacija se bo odprla v vašem spletnem brskalniku. Na levi strani izberite funkcionalnost, ki jo želite uporabiti.

### Uporaba

**Ustvarjanje novega kripto portfelja**

Za ustvarjanje novega kripto portfelja izberite možnost "Create Portfolio". Vnesite ime portfelja in kliknite enter.

**Dodajanje nove kriptovalute v kripto portfelj**

Za dodajanje nove kriptovalute v kripto portfelj izberite možnost "Add Coin". Izberite kriptovaluto in vnesite količino. Kliknite enter.

**Odstranjevanje kriptovalute iz kripto portfelja**

Za odstranjevanje kriptovalute iz kripto portfelja izberite možnost "Remove Coin". Izberite kriptovaluto, ki jo želite odstraniti, in kliknite na "Remove".

**Izračun skupne vrednosti kripto portfelja**

Za izračun skupne vrednosti kripto portfelja izberite možnost "Calculate Portfolio Value". Aplikacija bo izračunala skupno vrednost vašega portfelja na podlagi trenutnih cen kriptovalut.

**Ogled zgodovine kripto portfelja**

Za ogled zgodovine kripto portfelja izberite možnost "View Portfolio History". Aplikacija bo prikazala seznam vseh transakcij, ki so bile izvedene na vašem portfelju.

**Nastavljanje opozoril**

Za nastavitev opozoril izberite možnost "Set Alerts". Izberite tip opozorila (cena ali odstotek) in vnesite vrednost. Izberite kriptovaluto in kliknite na "Set Alert".

**Izvoz kripto portfelja**

Za izvoz kripto portfelja izberite možnost "Export Portfolio". Kliknite na "Export" in aplikacija bo izvozila vaš portfelj v datoteko JSON.

**Uvoz kripto portfelja**

Za uvoz kripto portfelja izberite možnost "Import Portfolio". Izberite datoteko JSON, ki vsebuje vaš portfelj, in kliknite na "Import".

### Dodatne informacije

* Aplikacija uporablja API CoinGecko za pridobivanje trenutnih cen kriptoval