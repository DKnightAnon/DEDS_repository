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

Rosidi, N. (n.d.). Clustering with scikit-learn: A Tutorial on Unsupervised Learning - KDnuggets. KDnuggets. https://www.kdnuggets.com/2023/05/clustering-scikitlearn-tutorial-unsupervised-learning.html

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


# PR9-2 Frequent Itemsets in Unsupervised Machine Learning

## Frequent Itemsets
Frequent Itemsets zijn rijen in de brondata dat vaak samen gepaard gaan. Bijvoorbeeld als een klant product X koopt, is het waarschijnlijk dat product Y ook gekocht wordt. 

Aan de hand van een vooraf bepaald Minimal Support Threshold (minsup) worden combinaties van items opgeslagen. 
![voorbeeld van een itemset database](../Assets/Week%209/Frequent%20Itemsets/example_itemset_database.png)

Vervolgens wordt van elke itemset de Support Count berekend : hoe vaak de itemset voorkomt in de totale verzameling itemsets (ook als gedeelte van een grote itemset)

Bijvoorbeeld {Bread, Milk, Diapers} komt in 2 van de 5 itemsets in bovenstaande afbeelding voor. Hiervoor geldt dus een support count van `2/5 X 100% = 40%` .

Als de support count berekend is wordt het vergeleken met de eerder behandelde minsup, en als dat groter is wordt het opgeslagen als een Frequente Itemset. 

## Association Rules
Met de Frequent Itemsets die bekend zijn willen we associaties kunnen maken. Ofwel, als product X in de set zit, moet product Y er ook in zitten. 

Bij een dergelijke Rule zijn twee waardes belangrijk : 
- Support : het percentage transacties waar de Rule waar is
- Confidence : Gegeven alle transacties met Itemset X, hoe vaak komt Itemset Y voor

Voorbeeld : Itemset X {Milk, Diapers} wordt vaak samengekocht met Y {Beer}. Itemset is dus {Milk, Diapers, Beer}. 
Met bovenstaande Itemset Database :
- 5 Frequent Itemsets
- {Milk, Diapers, Beer} komt 2 maal voor
  - Support : 2/5 X 100 = 40%
- {Milk, Diapers} komt 3 maal voor
  - Confidence : 2/3 X 100 = ~67%

   ### Association Rule Mining
   Met de vorige onderwerpen uitgelegd, is het doel nu om een set transacties te vinden waarbij de Support Count en de Confidence Count boven de minsup en minconf (Minimal Confidence Threshold) uitkomen.

   ### Apriori Principle

   ![Afbeelding dat het Apriori principle weergeeft](../Assets/Week%209/Frequent%20Itemsets/Apriori_Principle.png)

   Pseudocode : 
   ```
      L[1] = {frequent 1-itemsets};
      for (k=2; L[k-1] != 0; k ++) do begin
         // perform self-joining
         C[k] = getUnion(L[k-1])
         // remove pruned supersets
         C[k] = pruning(C[k])
         // get itemsets that satisfy minSup
         L[k] = getAboveMinSup(C[k], minSup)
      end
      Answer = Lk (union)
   ```

## Opdracht

PR9-2: Great Outdoors wil graag weten welke producten vaak samen gekocht worden door klanten, door het bouwen van Frequent Itemsets met A-Priori-algoritme. Tip: merge eerst de tabellen 'product' en 'order_details' om een juiste tabel met brongegevens te krijgen waarop je het algoritme kan toepassen. 
- Pas waar nodig Dummy Encoding toe.
- Train het initiële algoritme.
- Experimenteer met meerdere support & confidence thresholds.
- Gebruik [deze webpagina](https://towardsdatascience.com/apriori-association-rule-mining-explanation-and-python-implementation-290b42afdfc6) als inspiratie.

***
Chonyy. (2022, September 19). Apriori — association rule mining in-depth explanation and Python implementation. Medium. https://towardsdatascience.com/apriori-association-rule-mining-explanation-and-python-implementation-290b42afdfc6

GfG. (2023, January 11). Implementing Apriori algorithm in Python. GeeksforGeeks. https://www.geeksforgeeks.org/implementing-apriori-algorithm-in-python/

Poojari, D. (2023, July 13). Apriori algorithm in Python (Recommendation engine). Medium. https://deepak6446.medium.com/apriori-algorithm-in-python-recommendation-engine-5ba89bd1a6da

Madhushika, D. (2022, January 6). Apriori Algorithm in Data Mining: Part 02 - LinkIT - Medium. Medium. https://medium.com/linkit-intecs/apriori-algorithm-in-data-mining-part-2-590d58e0998b

Khan, A. (2024, April 10). Data Science - Apriori algorithm in Python- Market basket analysis. Intellipaat. https://intellipaat.com/blog/data-science-apriori-algorithm/

Bismakhan. (2021, October 14). Apriori Algorithm from Scratch. https://www.kaggle.com/code/bismakhan08/apriori-algorithm-from-scratch

Webmaster. (2024, March 6). The apriori algorithm in Python: Discover associations in data – meccanismo complesso. https://www.meccanismocomplesso.org/en/the-apriori-algorithm-in-python-discover-associations-in-data/

Raschka, S. (n.d.). Apriori - mlxtend. https://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/


   ### Implementatie

   - dummy encode PRODUCT_NAME (dataframe maken met net zoveel kolommen als er producten zijn)
   - maak een loop dat voor elk ORDER_NUMBER een list maakt van bestelde producten
     - Drop alles met maar 1 product?
   - vul dummy encode dataframe ( vul 1 in in kolommen waarvan order_detail een product van bevat)

   ### TODO
   - definitie geven voor verschillende termen(Support, Confidence, Lift, misschien ook Conviction)