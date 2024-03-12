# P4.1
Tijdens deze opdracht worden de dimensiewaardes vastgesteld op basis van het in week 1 opgestelde brongegevensmodel. Dimensiewaardes zijn mensen/dingen/objecten.


# P4.2
Tijdens deze opdracht wordt er voortgebouwd op P4.1 door de feittabellen vast te stellen. Feiten zijn gebeurtenissen/activiteite/processen dat vastgelegd worden met behulp van dimensiewaardes.

## Feit tabellen met foreign keys naar elkaar
1 van de opgestelde feittabellen (RETURNED_ITEM) heeft in de brongegevens een foreign key naar ORDER_DETAILS. Het is normaal niet de bedoeling dat feittabellen met elkaar verbonden zijn. Tegelijkertijd zijn de twee tabellen duidelijk andere gebeurtenissen, en kunnen ze niet samengevoegd worden. De docent kon ook geen antwoord geven op de vraag hoe deze situatie afgehandeld moet worden. Ik heb besloten om de foreign key verwijzen te laten staan. Dit is omdat RETURNED_ITEM echt niet zonder die foreign key kan.

## Afgeleide meetwaarden
Als gedeelte van de opdracht moeten er over de feittabellen in totaal 5 meetwaardes afgeleid worden. Meetwaardes zijn waardes in de tabel waar berekening over gedaan kunnen worden. Afgeleide meetwaarden zijn waardes dat niet in de tabel staan, maar wel opgesteld kan worden door al bestaande waardes te combineren.

De 5 afgeleide meetwaardes zijn : <br>
1. ORDER_DETAILS_TURNOVER in ORDER_DETAILS (UNIT_SALE_PRICE * QUANTITY)
2. ORDER_DETAILS_PROFIT in ORDER_DETAILS ( (UNIT_SALE_PRICE * QUANTITY)-(UNIT_COST * QUANTITY) )
3. ORDER_DETAILS_DISCOUNT_PERCENTAGE in ORDER_DETAILS ( (UNIT_SALE_PRICE/UNIT_PRICE) * 100)

# P4.3
Tijdens deze opdracht wordt op basis van de eerder opgestelde dimensiewaardes en feittabellen eerste een ETL-schema voor elke tabel gemaakt. Vervolgens moet er een database in Microsoft SQL Server Management Studio gemaakt worden wat uiteindelijk de Data Warehouse gaat worden. 

## Data verzamelen 

Data uit de brongegevens (aangeleverde sqlite databases en CSV bestanden) moeten vertaald worden naar feit- en dimensietabellen. Hiervoor moet de data in deze brongegevens ook opgeschoond worden. (De nieuwe SQLite bestanden op brightspace lijken schoon aangeleverd te zijn.)

Om deze tabellen op te stellen zal er gebruik gemaakt worden van Pandas om tabellen met elkaar te mergen, extra kolommen (afgeleide waardes) toe te voegen en overtollige kolommen te verwijderen.