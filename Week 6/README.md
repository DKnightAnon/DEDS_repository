# P6.1 Power BI

Week 6 gaat over Analyse & Rapportage. Door middel van Power BI (Microsoft Software) moet data inzichtelijk gemaakt worden. Data kan geïmporteerd worden vanuit SQL Server om in Power BI zogenaamde Visuals te maken. Data kan hier op verschillende manieren gecombineerd worden om bepaalde inzchten mogelijk te maken. 

## TO-DO
1. ~~Foreign Key naar ORDER_METHOD vanuit ORDER_DETAILS, naar RETURN_REASON vanuit RETURNED_ITEM~~
2. ~~Triggers schrijven om rekening te houden met nieuwe relaties~~
3. ~~relatie tussen order_details en product vergeten~~
4. ~~GO_SALES_INVENTORY_LEVELSData koppelen aan PRODUCT.Product_number~~
5. ~~GO_SALES_PRODUCT_FORECASTDAta koppelen aan PRODUCT.Product_number~~
![Power BI tabel-relaties](../Assets/Week%206/Power%20BI%20tabelrelaties%2018-3-2024.png)

## Power BI TO-DO
1. Pagina's aanmaken per management vraag
2. Opzoeken hoe je een hierarchie maakt
3. Product_Type en Product_Line uit Product halen om makkelijker een drill-down te kunnen maken?
4. Data opnieuw importeren in Power BI, sommige velden hebben nog NULL waardes.

## Opdrachten

Voer minimaal twee van de onderstaande opdrachten uit : 

1. **Maak een dashboard waarin je met verschillende meetwaarden en vanuit verschillende invalshoeken (dimensies) naar de teruggebrachte producten en de werkelijke orders kan kijken.**
2. Maak een dashboard waarin je met verschillende meetwaarden en vanuit verschillende invalshoeken (dimensies) naar de verkoopdoelen en de werkelijke orders kan kijken.
3. Maak een dashboard waarin je met verschillende meetwaarden en vanuit verschillende invalshoeken (dimensies) naar de trainingen en de werkelijke orders kan kijken.
4. Maak een dashboard waarin je met verschillende meetwaarden en vanuit verschillende invalshoeken (dimensies) naar de klanttevredenheidsenquête en de werkelijke orders kan kijken.
5. Maak een dashboard waarin je met verschillende meetwaarden en vanuit verschillende invalshoeken (dimensies) naar de verwachte orderaantallen en de werkelijke orders kan kijken.
6. **Maak een dashboard waarin je met verschillende meetwaarden en vanuit verschillende invalshoeken (dimensies) naar het voorraadniveau en de werkelijke orders kan kijken.**

## Management vragen
1. Hoeveel retouren zijn er per product, per product type, per reden, per klant  die verkocht is door een verkoper op een bepaald moment? 
2. Hoeveel orders zijn er in totaal afgehandeld, per branch, per employee en hebben de werknemers met de grootste aantallen orders een cursus gehad, zo ja dan welke cursus per employee? 
3. Hoeveel omzet is er in een jaar behaald, per product en per bestelmethode en wat waren  aantal producten die hierbij zijn verkocht  
4. Wat waren de opbrengsten en targets per kwartaal van elk product en welke employees hebben de target wel en welke hebben de target niet gehaald en welke cursussen hebben deze employees allemaal gevolgd? 
5. Welke retailer neemt de meeste producten af en welke retailer heeft de meeste omzet per jaar per maand? 
6. Waar (land en stad) worden jaarlijks de meeste producten verkocht en wat is de omzet hierbij en zijn er hierbij campaigns gehouden en indien ja hoeveel? 
7. Geef de aantal retouren van producten met de sales branch en return reason in verhouding met het aantal verkochte producten per maand. Is er een bestelmethode die meer retouren geeft dan andere? 