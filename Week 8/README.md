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

Versie 3, met outliers (Orderaantal boven 800) weggelaten. MSE van 2764.827458808092 en MAE van 31.848096998273398 .
![versie 2 van regressiemodel](../Assets/Week%208/Regressiemodel%20grafiek%20V2.png)

## Scatter plots
Atlassian. (n.d.). Mastering Scatter Plots: Visualize data correlations. https://www.atlassian.com/data/charts/what-is-a-scatter-plot 

How to plot regression line of sklearn model in matplotlib? -. (2023, August 25). ProjectPro. https://www.projectpro.io/recipes/plot-regression-line-of-sklearn-model-matplotlib 


TODO : 
- Herschrijf notebook om gebruik te maken van de Greatoutdoors Datawarehouse

# PR8-2 Classificatiemodellen in Machine Learning