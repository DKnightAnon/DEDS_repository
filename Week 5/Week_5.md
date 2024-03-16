# P5.1 Voortbouwing H4.P3

Zie Week 4 Practicum 3 voor details.

Er moet gekeken worden naar het formaat van datums in de brontabellen. Date en Datetime in SQL Server heeft namelijk een formaat van Jaar-Maand-Dag Uur-Minuut-Seconde. 

Het ETL schema zal als een ster schema gemaakt worden. Dat wil zeggen dat een feit tabel naar een dimensie kan verwijzen, maar dimensies kunnen onderling niet naar elkaar verwijzen. 

*Als dimensies naar elkaar kunnen verwijzen is er sprake van een Snowflake-schema.*

Er moet ook nog gekeken worden of elke dimensietabel een afgeleide waarde heeft.
Er moet rekening mee gehouden worden date het formaat voor datums in de brongegevens afwijkt van het formaat dat SQL Server gebruikt. 

## INSERT problemen
Bij de dimensie tabel Retailer treden er veel problemen op betreffende Insertion. Dit komt omdat veel winkelnamen (COMPANY_NAME) en adressen (ADDRESS1) een apostrof bevatten. In SQL server is dit een speciaal karakter dat het begin of einde van een string aanduidt. Dit zorgt voor problemen later in de insert statement.


# P5.2 - Converteren naar Slowly Changing Dimensions

In deze stap moeten Surrogate Keys geïmplementeerd worden. Surrogate Keys zijn alternatieve primaire sleutels dat gebruikt worden in plaats van de PK's in de brontabel. Een Surrogate Key bestaat uit een nummer, met een tweede kolom voor een timestamp(dit is niet gedeelte van de SK). Op deze wijze kan bij elke wijziging op een rij een duplicaat aangemaakt worden met de gewijzigde gegevens. Dat wilt zeggen dat je de originele rij en de gemodificeerde rij beide in de tabel houdt. Met behulp van de SK en de timestamp kun je zo wijzigingen over een bepaalde periode van tijd bijhouden. 

## Surrogate Keys
Een SK vervangt de FK. Maar hoe weet de Feittabel dat het de nieuwe, gewijzigde record in de dimensie tabel moet hebben? Misschien is dit te doen door de Foreign Key en de Foreign Surrogate Key te combineren in combinatie met een Trigger of Stored Procedure. Als ~~de Dimension gewijzigd~~ er nieuwe informatie ingevoerd wordt, kan er een Trigger geactiveerd worden dat op basis van de Foreign Key gaat zoeken naar de Foreign Surrogate Key met het meest recente timestamp.

## Hoe behoud je de juiste verwijzing naar de juiste Foreign Surrogate Key (FSK)

In de brontabellen heb je Primary Keys en Foreign Keys. De verwijzingen naar andere tabellen gebeurt met het gebruik hiervan, en deze waardes hebben een zinvolle betekenis voor de bedrijfgang.

Surrogate Keys worden echter pas toegevoegd in de Data Warehouse. Hierdoor heb je geen zinvolle waardes om een PK-FK relatie op te baseren. Maar misschien kan dit gedaan worden door in de CREATE TABLE statements gebruik te maken van DEFAULT values of TRIGGERS. 

Op het internet zoeken naar (Foreign) Surrogate Keys levert alleen resultaten op over het concept, maar niet de implementatie. Misschien googlen naar specifiek Slowly Changing Dimensions?

### Triggers gebruiken om FSK's te selecteren

- Trigger INSTEAD OF insert
- Zoek in dimensie tabel op FK, selecteer rij met FSK waarvan timestamp voor feit plaatsvond, maar niet na
- Zet 


## Date Dimensie
Ik heb besloten om de date dimension niet te gebruiken. Ik heb mijn handen vol aan de surrogate keys, en ik wil niet nog meer tijd kwijt zijn aan het implementeren van de date dimensie. Ik snap wat de meerwaarde is (op basis van de datum opslitsen in eenheiden zoals dag van de week), maar niet hoe je het het best kan implementeren.


# P5.3 - Conversatie naar Executable

In deze stap moet het Jupyter Notebook project omgezet worden naar een Python project.
(Jupyter Notebook is niet specifiek voor Python - Het is gebouwd met HTML, CSS en Javacsript en kan codeblokken bevatten voor verschillende talen.)

Het converteren van Jupyter Notebook naar Python code is handig omdat je dan een executable hebt dat op een server uitvoerbaar is. 

## Python project folder structuur

![Folderstructuur](../Assets/Week%205/Folderstructuur_Pythonproject.png)



## Duplicate entries bij meerdere runs van datastraat

Zoals ik het begrijp pakt de datastraat alle gegevens in de brontabellen en voegt het ze toe aan de Data Warehouse. Een logisch gevolg is dan dat als je de straat een 2e keer runt(ook al zitten er nu nieuwe rijen bij) het opnieuw alle gegevens in de brontabellen pakt. 

Stel dat ik Rij 1 en Rij 2 heb, met 5 waardes elk. Ik run de datastraat waardoor ze nu in SQL Server staan, en pas de waarde van kolom 1 aan en run de datastraat opnieuw. 
Nu heb ik 4 rijen in de Data Warehouse, in plaats van de 2 originele en de gewijzigde tabel. 

Mijn zorg is dat als ik de datastraat meerdere keren run, een wijziging overschreden kan worden. Om het voorbeeld hierboven te gebruiken, ben ik bang dat de wijziging die tijdens run 2 in de datawarehouse is geplaatst ongedaan wordt tijdens run 3. 
Maar is mijn denkwijze niet fout hier? Data Warehouses zijn voornamelijk read-only (Een beetje vergelijkbaar met Ledgers zoals in de financiele wereld). Als er iets aan de gegevens aangepast wordt gebeurt dat niet in de Warehouse, maar in de brongegevens. 

Gebruik de brongegevens als startpunt. 

## Logging
Maak gebruik van Loguru : ``poetry add loguru``





# Vragen om te stellen

1. De data in het Datawarehouse wordt niet direct daar aangepast. Elke wijziging in de gegevens moet uit de brontabel komen. Als er in een dimensie tabel iets wordt aangepast moet het bijbehorende feit ook aangepast worden, dus komt er dan in de feittabel en in de dimensie een nieuwe regel?
    - Als dit klopt en het feit en de dimensie tegelijk worden ingevoerd, kan ik de Foreign Surrogate Key dan niet selecteren op basis van de meest recente entry in de dimensie tabel?
2. Als ik de datastraat run, hoe voorkom ik dat ik duplicate entries krijg? Als alles in de rij behalve de Surrogate Key precies hetzelfde is, kan ik de rij dan weglaten?

3. Logger.info() moet met een eigen bericht in het jupyter notebook bestand geplaatst worden?
4. Hardcoded variables moeten volgens de powerpoint in een List. Is het dan de bedoeling dat in script.py alle variabelen vervangen moeten worden met LIST_NAME[KEY]?
5. Aan het begin van mijn jupyter notebook heb ik code dat de brongegevens inlaadt. Moet ik dit in script.py aanpassen zodat het wijst naar data/raw/brongegeven? 