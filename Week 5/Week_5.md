# P5.1 Voortbouwing H4.P3

Zie Week 4 Practicum 3 voor details.

Er moet gekeken worden naar het formaat van datums in de brontabellen. Date en Datetime in SQL Server heeft namelijk een formaat van Jaar-Maand-Dag Uur-Minuut-Seconde. 

Het ETL schema zal als een ster schema gemaakt worden. Dat wil zeggen dat een feit tabel naar een dimensie kan verwijzen, maar dimensies kunnen onderling niet naar elkaar verwijzen. 

*Als dimensies naar elkaar kunnen verwijzen is er sprake van een Snowflake-schema.*

Er moet ook nog gekeken worden of elke dimensietabel een afgeleide waarde heeft.


# P5.2 - Converteren naar Slowly Changing Dimensions

In deze stap moeten Surrogate Keys geïmplementeerd worden. Surrogate Keys zijn alternatieve primaire sleutels dat gebruikt worden in plaats van de PK's in de brontabel. Een Surrogate Key bestaat uit een nummer, met een tweede kolom voor een timestamp(dit is niet gedeelte van de SK). Op deze wijze kan bij elke wijziging op een rij een duplicaat aangemaakt worden met de gewijzigde gegevens. Dat wilt zeggen dat je de originele rij en de gemodificeerde rij beide in de tabel houdt. Met behulp van de SK en de timestamp kun je zo wijzigingen over een bepaalde periode van tijd bijhouden. 


Een SK vervangt de FK. Maar hoe weet de Feittabel dat het de nieuwe, gewijzigde record in de dimensie tabel moet hebben? Misschien is dit te doen door de Foreign Key en de Foreign Surrogate Key te combineren in combinatie met een Trigger of Stored Procedure. Als de Dimension gewijzigde wordt, kan er een Trigger geactiveerd worden dat op basis van de Foreign Key gaat zoeken naar de Foreign Surrogate Key met het meest recente timestamp.


# P5.3 - Conversatie naar Executable

In deze stap moet het Jupyter Notebook project omgezet worden naar een Python project.