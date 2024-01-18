# League of Legends Champion Tier List Scraper

## Uzdevums

Atrasts labāko tēlo katrā pozīcijā apskatot 6 statistikas avotus un apvienojot statistiku no viņiem visiem, pārskatāmā veidā, lai varētu būt informēts par to kas šobrīd ir labs.


## Programmas darbība

Šī programma izmanto Selenium bibliotēku, lai webscrape datus no sešiem populāriem League of Legends statistikas avotiem (u.gg, metasrc.com, op.gg, lolalytics.com, blitz.gg un mobaliytics.gg), ievācot informāciju no viņu izveidotajiem līmeņu sarakstiem nolasot informāciju par katru tēlu tajā (tier list) par to cik katrs tēls ir labs dažādās pozīcijās, tad šī programma katrā no statistikas avotiem pievieno katram līmenim savu vērtību(šo ir nepieciešams katrai tīmekļai vietnei darīt atsevišķi, jo ir dažāds līmeņu skaits), pēc tam ievieto šo statistiku excelī izlīdzinot līmeņu vērtības tā lai vidēji tēlam būtu vērtība 1 (lai samazinātu kāda konkrēta statistikas avota ietekmi uz tēla "vērtību"), kad ir iziets cauri visiem statistikas avotiem un katram tēla piešķirta vērtība, aprēķina katra tēla vidējo vērtību.

**Prgramma jāpalaiž ar main.py failu, kas savukārt palaidīs funkcijas pārējos failos**

## Python Bibliotēkas

Programma izmanto šādas Python bibliotēkas:

1. **Selenium**: Automatizē pārlūkprogrammas darbību, lai iegūtu datus no  mājaslapām.

2. **time**: Nodrošina aizkaves funkcijas, lai kontrolētu pārlūkprogrammas darbības laiku un pagaidītu, kamēr lapas ielādējas.

3. **openpyxl**: Ļauj iegūt un apstrādāt Microsoft Excel failus, kurā tiek saglabāti dati par tēliem.

Lai instalētu šīs bibliotēkas, izpildiet komandas:

```bash
pip install selenium 
pip install openpyxl
```

