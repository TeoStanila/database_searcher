# Writeup

## 3.1 Approach

Soluția mea conține 3 componente la nivel înalt:
```text
Generare de Date
   ↓
Antrenarea Modelului
   ↓
Inferența Modelului
```
Pentru comenzile necesare rulării soluției, vedeți "README"

## Generarea de Date
Datasetul folosit în acest task are este de forma (query - indici_relevanți), unde "query" reprezintă cerința utilizatorului iar "indici_relevanți" indicii documentelor relevante pentru acea cerere.

"lookup.py" e un script care filtrează documentele din baza de date dupa atribtele lor, la nevoia utilizatorului. La final întoarce indicii relevanți. în subfolderul "lookups" se află toate valorile câmpurilor din dataset pentru a putea genera date cât mai complete.

Cu "data_generation.py" se obține cealaltă jumătate de dataset, adică query-urile. Pornește de la un template care conține in mijloc un cuvânt de tipul "business", la care adaugă în fața sau în spatele acestuia diverși filtri. Prezența cuvintelor și ordinea lor sunt determinate aleatoriu.

Pentru celelalte query-uri am luat exemplul conceptelor complexe din enunțul taskului și le-am mapat manual după sensul cuvintelor. Cu această mapare, fiecare query specifică locația, marketul și este exprimată printr-o idee complexă (exp: agile startups).

---

## Antrenarea Modelului
Soluția problemei presupune fine-tuningul unui model deja existent, în cazul acesta "all-MiniLM-L6-v2", ales pentru dimensiunea și timpul de execuție redus. De asemenea, acest model a produs cele mai bune rezultate când a fost testat ca un simplu baseline care doar încodează query-ul și documentele, făcând produs scalar între ele. Inițial voiam ca modelul să fie antrenat cu un layer final cu 477 de neuroni, numarul de documente din dataset. Totuși, acest design nu este suficient de scalabil deoarece orice adiție sau ștergere din dataset presupune reantrenarea modelului.

În schimb, modelul este antrenat pentru a reproduce embedding-uri de query-uri și de documente. Astfel, modelul aduce reprezentarea unui query cât mai aproape de embedding-ul documentelor pentru a avea un scor de similaritate mai mare.

Cu acest design, modelul este mai robust la date pe care nu le-a văzut în timpul antrenării.

## Inferența Modelului

Această componentă așteaptă un query de la utilizator după care returnează primele 5 companii relevante pentru acesta.


## 3.2 Tradeoffs

În primul rând am vrut ca modelul să fie robust la date noi. Un model cu o nișă atât de specifică (un dataset de 477 de documente și nimic altceva) nu este o soluție bună deoarece nu reflectă lumea reală, în care datele sunt rareori statice.

De asemenea, am vrut ca antrenarea și inferența să decurgă relativ rapid, așa că am optat pentru finetuning în loc de a antrena un model de la zero. În plus, un model deja antrenat are cunoștințe denerale de limbaj, astfel că finetuningul doar îl rafinează pentru acest set specific de date.

Un trade-off intenționat pe care l-am făcut este viteză - acuratețe. Am generat doar 300 de perechi query-indici, dimensiune care nu produce cea mai adecvată antrenare. În producție, un model de acest tip va fi antrenat și testat pe un dataset semnificativ mai mare (>10x), având inerent o acuratețe mai bună.

---

## 3.3 Error Analysis

Modelul încă are probleme în a distinge conceptul de "în afara". Uitați rezultatele query-ului "companies outside romania" pentru baseline:
| Similaritate | Companie |
|------------------:|---------|
| 0.575 | Bunge Romania |
| 0.568 | METRO România |
| 0.559 | CBRE Romania |
| 0.541 | STILL |
| 0.498 | European Drinks |

cât și pentru modelul antrenat:
| Similaritate | Companie |
|------------------:|---------|
| 0.499 | Bunge Romania |
| 0.451 | Mercedes-Benz Trucks & Buses Romania |
| 0.424 | METRO România |
| 0.402 | Unilever |
| 0.395 | Teqniq |

METRO și Bunge rămân în top, în timp ce STILL și CBRE sunt înlocuite de Unilever și Merceds-Benz. E de notat totuși că a 5-a prezicere "Teqniq", chiar se află în afara României fiind o companie finlandeză. Deci modelul devine relativ mai precis, dar volumul de date nu a fost suficient de mare încât să facă destingerea mai bine. O antrenare axată mai precis pe aceste exemple, poate cu positive weighting ar face rezultatele mai bune.

De asemenea, testele pe query-urile mai complexe produce rezultate mixte. Modelul înțelege des relațiile spațiale (ce înseamnă Scandinavia, Europa de Est etc...). Acestea sunt rezulattele modelului la query-ul "Renewable energy equipment manufacturers in Scandinavia":
| Similaritate | Companie |
|------------------:|---------|
| 0.665 | Enercon |
| 0.634 | windainergy |
| 0.634 | windainergy |
| 0.628 | Pellbin Turbine |
| 0.626 | Tesla Ocean Turbine |

Toate companiile îndeplinesc condițiile query-ului.

Dar la alte query-uri, precum "Construction companies in the United States with revenue over $50 million", se pierd:
| Cosine similarity | Company |
|------------------:|---------|
| 0.549 | Trusted Solutions Group |
| 0.500 | MA-Engineering |
| 0.470 | Colaska |
| 0.437 | Agir&Tude |
| 0.435 | EMCOR Group |

Agir&Tude și MA-Engineering sunt firme din Franța și, respectiv, Elveția.

---

## 3.4 Scaling

În primul rând, datasetul de antrenament al modelului ar fi semnificativ mai mare.

În al doilea rând, 100,000 de documente ar afecta foarte mult inferența deoarece va trebui să calculeze similaritatea dintre query si 100,000 de documente, în loc de 500. Astfel cred că o variantă mai bună ar fi un algoritm de tip K-means pentru a vedea un clusterele cu care query-ul se potrivește, calculând ulterior similaritățile.

O altă opțiune este schimbarea structurii datelor. O structură de tipul (Anchor, Positive, Hard Negative) ar ajuta modelul să distingă mai bine între cazurile adevărate și pe cele aproape adevărate.

---

## 3.5 Failure Modes

Sistemul ar putea reproduce rezultate greșite dar cu mare încredere la firmele extrem de asemănătoare. O firmă de fintech înființată după 2000 din Romania este aproape identică cu una de fintech înființată după 2000, dar din Bulgaria. Fiecare câmp este tratat drept la fel de important în antrenare, așa că modelul va vedea o intersecție între cele 2 firme descrise, putând foarte ușor să o recomande pe una ăn loc de cealaltă.

Pentru a detecta acest tip de probleme, aș urmări cazurile cu scoruri mari, dar marcate drept incorect ca utilizatori și aș optimiza mai mult precizia pentru a avea mai puține pozitive false.

Structura (Anchor, Positive, hard Negative) este de asemenea folositoare pentru a distinge aceste cazuri.