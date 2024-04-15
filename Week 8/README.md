# PR8-1 - Regressiemodellen in Machine Learning


[![Grafiek van een Regression Model](../Assets/Week%208/Linear%20Regression.png)](https://builtin.com/data-science/regression-machine-learning)


afhankelijke variabele uit GO_SALES_PRODUCT_FORECASTData halen? onafhankelijke data uit GO_SALES.sqlite?


onafhankelijke variabelen samenstellen. Order_header_order_details en product uit GO_SALES.sqlite combineren om per product per maand per jaar het aantal verkochte exemplaren te berekenen. *Hoe past het CSV bestand hierin? bestellen gaan over dezelfde periode als de voorspelling.*

Regressiemodellen hebben tussenwaardes (dat wil zeggen, het kan decimalen hebben). Wat is dan een goede afhankelijke  variabele? Niet aantal verkocht, dat kan alleen op hele nummers uitkomen.

![evaluatie van een regressiemodel](../Assets/Week%208/Modellen_evalueren.jpg)
*Slide waarin het evalueren van regressiemodellen wordt uitgelegd*

Het lijkt erop dat de te voorspellen waarde naast de actuele waarde wordt geplaatst. Is dit puur voor tijdens het testen? 

2-4-2024 - Momenteel bestaat de trainset uit Productnumber -> Year -> Month -> Quantity, waarbij de eerste 3 genest zijn. Per Month zijn alle aankopen op de dagen in die maand bij elkaar opgeteld. Dit is gedaan om op hetzelfde aantal rijen als in GO_SALES_PRODUCT_FORECASTData te komen. Wat als dit niet gedaan wordt? Dan zou ik meer kolommen kunnen gebruiken om patronen te zoeken, zoals ORDER_METHOD_CODE. 

*Resultaat van Groupby te gebruiken om op hetzelfde aantal dataframes uit te komen als in GO_SALES_PRODUCT_FORECASTData*
![Nested Rows in dataframe](../Assets/Week%208/Nested%20Rows%20in%20dataframe.png)


## Evaluatie
![Gegenereerde grafiek van de voorspelde verwachte hoeveelheden in een order](../Assets/Week%208/Regressiemodel%20grafiek.png)

**Dit is een grafiek met informatie van jaartallen 2020,2021,2022. Misschien is het iets minder chaotisch als het tot 1 jaartal beperkt wordt?**

Bovenstaande afbeelding is de opgestelde grafiek dat voorspelt welke hoeveoelheden verkocht worden. Zoals te zien zijn meeste datapunten te vinden aan de linkerkant, met een paar *outliers* aan de rechterkant. Door de hoeveelheid kleine orderaantallen in de brondata is ook te zien dat het gros van de voorspellingen niet boven 65 producten uitkomen. In de brondata zijn echter ook grote orderaantallen in de honderd- en duizentallen te vinden.

Dit model heeft een Mean Squared Error (MSE) van 3842.5293789575953, en een Mean Absolute Error (MAE) van 35.28974416446006. 

Dit zijn de onafhankelijke variabelen : 
- Product Number
- Year
- Month
- Order_Method_Code
- Product_Type_Code

met als afhankelijke variabele : 
- Quantity

Door onafhankelijke variabelen UNIT_COST, UNIT_SALE_PRICE, en RETAILER_ID(Retailer_Name gemapped naar integers) toe te voegen is een MSE van 3554.6285912992025 en een MAE van 33.391287240728445 behaald.

Versie 2, met outliers (Orderaantal boven 800) weggelaten. MSE van 2764.827458808092 en MAE van 31.848096998273398 . Variance score / Root Mean Squared Error (RMSE) van 52.58162662763574 .
![versie 2 van regressiemodel](../Assets/Week%208/Regressiemodel%20grafiek%20V2.png)
![historogram van residuele data](../Assets/Week%208/Residuals_Historogram.png)

06-04-2024-20:35 - Versie 3 van model gemaakt. 
- MSE : 2804.0034939106513
- MAE : 31.969058132392767
- RMSE : 52.95284217028064
![versie 3 regressiemodel](../Assets/Week%208/Regressiemodel%20grafiek%20V3.png)




## Scatter plots
Atlassian. (n.d.). Mastering Scatter Plots: Visualize data correlations. https://www.atlassian.com/data/charts/what-is-a-scatter-plot 

How to plot regression line of sklearn model in matplotlib? -. (2023, August 25). ProjectPro. https://www.projectpro.io/recipes/plot-regression-line-of-sklearn-model-matplotlib 

## Linear regression

Lineaire Regressie werkt door **LEG UIT**


Surmayi. (2024, February 26). Linear regression using Pandas & Numpy — for beginners in data science. Medium. https://medium.com/analytics-vidhya/linear-regression-using-pandas-numpy-for-beginners-in-data-science-fe57157ed93d

A beginner’s guide to Linear Regression in Python with Scikit-Learn. (2020, September 20). The AI Dream. https://www.theaidream.com/post/a-beginner-s-guide-to-linear-regression-in-python-with-scikit-learn

TODO : 
- Herschrijf notebook om gebruik te maken van de Greatoutdoors Datawarehouse
- Linear Regression plotline toevoegen

# PR8-2 Classificatiemodellen in Machine Learning

De opdracht is om een classificatiemodel te maken dat voorspeld wat de retourreden gaat zijn voor toekomstige order, gebaseerd op reeds bekende data. 

Met dat in gedachte, is de afhankelijke variabele GO_SALES.Returned_Item.Return_Reason_Code.
Verwachte onafhankelijke variabelen zijn : 
- Order_header.order_date
- returned_item.return_date
- order_method.order_method_code

Momenteel ziet de confusion matrix er als volgt uit : 
![Confusion Matrix versie 1](../Assets/Week%208/Confusion%20Matrix%20V1,%20Depth=MAX.png)

Dit ziet er heel anders uit dan dat uit de demo van het hoorcollege : 
**AFBEELDING HIER**

In eerste instantie dacht ik dat ik iets fout had gedaan. Maar dit verschil in de matrices komt volgens mij omdat de voorspelde resultaten van de opdracht niet binair zijn, in tegenstelling tot het voorbeeld. In het voorbeeld kan de voorspelde waarde 0 of 1 zijn, en niks anders. Daarmee kom je inderdaad op een nette matrix van 2x2 terecht. 
De resultaten vanuit de opdracht kunnen elk gegeven positief getal zijn, wat voor meer blokken in de matrix zorgt. 

Dit misverstand zorgde er ook voor dat ik deze foutmelding kreeg : 
**AFBEELDING** Ik probeerde maar 2 labels mee te geven, terwijl er veel meer blokken zijn dan dat.

Er moet gekeken worden naar hoe de confusion matrix kleiner gemaakt kan worden. Dat wil zeggen, afhankelijk van of de voorspelling klopt moet het in een True Positive, True Negative, False Positive of False Negative terecht komen. Op deze wijze moet de matrix binair gemaakt worden. 

**ER MOET GEZOCHT WORDEN OP RETURN_REASON, NIET RETURN_QUANTITY**

4-4-2024-14:46 - accuraatheidscore is momenteel 99+%. Komt dit vanwege de join tussen order_details en returned_item? Niet elke order wordt (in zijn geheel) geretouneerd. Als de return_reason NaN is, waar wordt het dan naar veranderd? *besloten om NaN naar 6 te veranderen voor One-Hot encoding*

Momenteel krijg ik een 6x6 Confusion Matrix : 
![6x6 confusion matrix betreffende retourredenen](../Assets/Week%208/Confusion%20Matrix%20V3,%20Depth=2.png)

Andere studenten is het gelukt om er een 2x2 matrix van te maken. *Met Damion Gans gesproken, 6x6 is het juiste formaat. Hoge accuraatheid is ook niet perse een fout.*

Dit heeft echter een verdacht hoog accuraatheidspercentage : namelijk 0.9907120743034056, ofwel 99%. Hier moet wel sprake zijn van een geval van *overfitting*. 

4-4-2024-15:40 - Na wat rondgespeeld te hebben met de onafhankelijke variabelen is het percentage nooit lager dan 98% gevallen. Het enige wat ik me kan bedenken is dat ik mijn joins op de tabellen niet goed doe. Niet elke Order_Detail heeft een bijbehorend Returned_Item in de database. In andere woorden, omdat er zoveel niet geretouneerd worden beinvloedt dat de conclusies dat het machine learnin model trekt.

Andere studenten zitten tussen de 40-60%. Misschien gebruiken zij de Order_Details tabel niet. Of misschien hebben zij enkel een left join gedaan zodat er alleen daadwerkelijk geretouneerde producten behandeld worden.

6-4-2024-7:31 - Onderstaande afbeelding is dezelfde 6x6 matrix gegenereerd via dezelfde code op depth=2, maar nu zijn de orders dat nooit teruggebracht zijn buiten beschouwing gelaten. 
![6x6 confusion matrix betreffende retourredenen, zonder nooit teruggebrachte orders](../Assets/Week%208/Confusion%20Matrix%20V4,%20Depth=2.png)


***
Training, P. (2023, May 12). Confusion Matrix with Scikit-Learn and Python - Pierian Training. Pierian Training. https://pieriantraining.com/confusion-matrix-with-scikit-learn-and-python/

Binary Classification Using a scikit Decision Tree -- Visual Studio Magazine. (2023, February 21). Visual Studio Magazine. https://visualstudiomagazine.com/articles/2023/02/21/scikit-decision-tree.aspx

Multilabel-indicator is not supported for confusion matrix. (n.d.). Stack Overflow. https://stackoverflow.com/questions/46953967/multilabel-indicator-is-not-supported-for-confusion-matrix

Kundu, R. (2023, May 11). Confusion Matrix: How To Use It & Interpret Results [Examples]. V7. https://www.v7labs.com/blog/confusion-matrix-guide

Is there a way to implement a 2x2 confusion matrix for multilabel classifier? (n.d.). Stack Overflow. https://stackoverflow.com/questions/70705556/is-there-a-way-to-implement-a-2x2-confusion-matrix-for-multilabel-classifier