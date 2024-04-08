# PR9-1 Clusteringmodellen in Unsupervised Machine Learning

Supervised en Unsupervised modellen verschillen is dat bij de eerste je de voorspellingen kan controlleren op waarheid. Bij Unsupervised moet je de resultaten van het model accepteren zoals ze zijn. De kwaliteit van de berekeningen kunnen echter wel nagekeken worden. 

Classificatie is het onderbrengen van een praktijksituatie / individu in een bepaalde *klasse*. Deze klassen zijn al bekend, en het model wordt getraind om per datapount op dezelfde klassen uitkomt.

Bij clustering is het doel om onbekende klassen te vinden. Het model moet zelf klassen vinden en/of maken zonder menselijke input.

Clustering kan toegepast worden waar labels/klassen onbekend, onzeker of te duur zijn. Bijvoorbeeld bij de volgende sectoren : 
- **Marketing** : groepen van zelfde soort klanten
- **Sterrenkunde** : groepen van zelfde soort sterren / zonnestelsels
- **DNA-onderzoek** : groepen genen met gelijksoortig effect
- **ChatGPT 3.5** : alle woorddelen zijn geclustered in een supergrote hoeveelheid dimensies om betekenis aan worden en zinnen te kunnen verlenen.


## K-means clustermodel

Demo stappen
1. bibliotheken importeren
   - sklearn.cluster
2. Data inlezen en kolommen selecteren
3. one-hot encoding
4. data samenvoegen
5. clustermodel bouwen
   - demo gebruikt 2 dimensies(variabelen)

***
Kim, C. (2022, July 28). Quick Guide to K-Means Clustering with Python example(Scikit-learn). Medium. https://medium.com/@chyun55555/quick-guide-to-k-means-clustering-with-python-example-scikit-learn-6efe8e319893

Python, R. (2023, August 4). K-Means Clustering in Python: A Practical Guide. https://realpython.com/k-means-clustering-python/

https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html

## Opdracht

PR9-1: Great Outdoors wil graag weten in welke segmenten verkoopafdelingen (‘sales_branches’) opgedeeld kan worden. Er bestaan al retailersegmenten (table ‘retailer_segment’), Great Outdoors wil dus óók segmenten creëren voor verkoopafdelingen.
- Pas waar nodig Dummy Encoding toe.
- Train het initiële clustermodel.
- Experimenteer met meerdere k’s door het berekenen van de inter- en intraclusterafstand.


Gebruikte databases : 
- GO_SALES.sqlite
  - sales_branch
    - country_code

***
**TODO** : 
- gebruikte variabelen aanvullen
- afbeeldingen toevoegen