# Neural Networks - Deel 1

Tijdens deze week is de opdracht om zelf een Neural Network te bouwen. Omdat er weinig tijd hiervoor beschikbaar is, is het de bedoeling dat je gebruik maakt van Generative AI (Dit ga ik niet doen.) Vanwege dit tijdslimiet is de hoofdzaak ook om enkel een begrip van het ondwerp op te doen.

Neurale Netwerken zijn fundamenteel binnen het gebied van kunstmatige intelligentie. ChatGPT is hier een voorbeeld van. 

## Uitleg

### Neural Networks
Neural Networks zijn een machine-learning model gemodelleerd op de structuur van het menselijke brein. Het neemt Input in, verwerkt dit met diverse Berekeningen, en genereert Output.

Neurale Netwerken zijn goed in het identifieceren van patronen uit een grote verzameling data, zelfs data waar geen lineaire verbindingen tussen staan. 
Het is in staat om input te classificeren en nieuwe data te generen.

Een Neuraal Netwerk bestaat uit Layers, waarbij 1 laag een verticale kolom met circkels vertegenwoordigd. Er zijn altijd 1 Input layer en 1 Output Layer, en daartussen bevindt zich 1 of meer Hidden Layers. Deze Hidden Layers voeren berekeningen uit op de invoergegevens, waardoor patronen in de data herkend kunnen worden.

### Trainen
Tijdens het trainen wordt er per keer 1 record van de dataset meegegeven als input. Deze input wordt dan door het netwerk verwerkt en tot een antwoord vervormd worden. 

### Overfitting







# Neural Networks - Deel 2


## Connecties

De nodes in de lagen van een Neuraal Netwerk werken samen om uiteindelijk een output te genereren. De Nodes in de lagen vormen connecties met elkaar om berekeningen uit te voeren. Het aantal connecties kan berekend worden door de hoeveelheid nodes in elke laag met elkaar te vermenigvuldigen. 
![](../Assets/Week%2010/Deel%202/Connections%20in%20a%20neural%20network.png)
In bovenstaand voorbeeld is er een Input layer met 6 nodes, een Hidden layer met 8 Nodes, en een  output layer met 4 Nodes. Dit komt neer op 6X8X4=192 connecties in dit Netwerk.

## Architectuur

Neural Networks zij er in verschillende soorten en maten. Ze kunnen van elkaar verschillen in de volgende aspecten : 
- Aantal input Nodes
- Aantal output Nodes
- Aantal hidden Layers
  - Aantal Nodes per hidden layer
- Nodes zijn wel of niet "fully connected" 
  - Nodes zijn fully connected als ze connecties hebben met alle Nodes in de volgende Layer
- sequentieel Neural Network (NN is verbonden met een tweede NN)
- Recurrent Connections
  - Er is sprake van Recurrent Connections als Nodes connecties heeft met niet alleen de volgende Layer, maar ook de vorige.

## Hidden Layers

De vereiste hoeveelheid Hidden Layers hangt af van de compelexiteit van de taak. 
Voor simpelere taken zoals binary classification of regressie voldoet 1 hidden layer vaak. Complexere taken zoals beeldherkenning zijn er vaak 2 of meer layers nodig.  

Naarmate de hoeveelheid hidden layers groter wordt, worden de uitkomsten ook steeds beter. Echter neemt de vereiste rekenkracht ook toe. Vandaar is het een zaak om niet een overbodige hoeveelheid layers te gebruiken.

Zodra er 3 hidden layers zijn, is er sprake van een Deep Neural Network. 


# Bouwen van een Neural Network

Prompt requirements
1. NN heeft 4 input nodes, 1 hidden layer met een door de student gekozen aantal nodes en 1 output node.
2. Gebruik 1 tot 5 input datapunten met bijbehorende output (antwoorden)
3. Maak gebruik van arrays
4. Laat de LLM code opleveren in C# of Java
5. We raden het niet aan maar voor de Python die-hards, mag het ook in Python. Echter,
zorg dat je of Numpy gebruikt als library of, een andere structuur die arrays vervangt. Zie
de opmerking hieronder voor meer info hierover.
6. Gebruik geen externe bibliotheken voor het bouwen van het neurale netwerk, met
uitzondering van #5 als je daarvoor kiest.
7. Instrueer de LLM dat het geen backpropagation mag gebruiken en ook niet Gradient
Descent algoritme. Vraag of het een simpele manier kan gebruiken op basis van de
‘error’ om de gewichten te trainen. Zie hoofdstuk Trainen verder in het document

prompt : 

```
give me code for a simple neural network built without external libraries, written in C#. It should have 4 input nodes, 1 hidden layer with 3 nodes, and 1 output node. do not use backpropagation or Gradient Descend
```

In de opdrachtbeschrijving staat dat er 1 tot 5 datapunten gegeven moeten worden. Een dergelijk datapunt moet 1 rij uit een database tabel zijn.
![rij uit tabel wordt als input gegeven voor netwerk](../Assets/Week%2010/Input_Data.png)
In de bovenstaande afbeelding zijn er in de input layer 4 Nodes. Dit betekent dat je elke keer dat je een input geeft, 1 input met 4 waardes aan het netwerk voedt. 

***
Alves, L. S. (2021, December 12). Building a simple neural network in C# - Analytics Vidhya - Medium. Medium. https://medium.com/analytics-vidhya/building-a-simple-neural-network-in-c-7e917e9fc2cc

Yen, L. (2024, February 2). Building a neural Network in Excel: A 6 step How-To Guide. Datamation. https://www.datamation.com/big-data/neural-network-in-excel/

Datumo. (2022, May 27). Understanding input data shapes for neural networks in TensorFlow KERas. DATUMO. https://blog.datumo.com/en/ai_tech/16035

Neural Network Regression from Scratch Using C# -- Visual Studio Magazine. (2023, October 18). Visual Studio Magazine. https://visualstudiomagazine.com/Articles/2023/10/18/neural-network-regression.aspx

Maze, C., & Maze, C. (2024, April 4). Different ways to add values to a C# array. Code Maze. https://code-maze.com/add-values-to-csharp-array/