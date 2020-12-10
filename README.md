# Tekstanalyse reviews Bol.com
Door de komst van het coronavirus zijn veel winkels gesloten, hierdoor is het aantal online aankopen in 2020 gestegen met 25% ten op zichte van dezelfde periode in 2019. Door middel van analyses in Python zal er onderzocht worden wat deze toename betekent voor de reviews over de Nederlandse webshop Bol.com. 
## Vereisten
Voor de analyse is gebruik gemaakt van de volgende software versies:
* Python 3.6.6
* Jupyter Notebook 6.0.3
## Inhoud
* `records_2019` bevat alle verzamelde reviews voor de maanden maart tot en met november. Deze zijn geordend op basis van de titel, de datum waarop deze geplaatst is, het aantal sterren dat gegeven is en de inhoud van de review. 
* `records_2020` bevat alle verzamelde reviews voor de maanden maart tot en met november. Deze zijn geordend op basis van de titel, de datum waarop deze geplaatst is, het aantal sterren dat gegeven is en de inhoud van de review.  
* `sterren` verwijst naar de sterrating die is gegeven door de consumenten van Bol.com. Deze zijn uiteenlopen van 1 ster tot 5 sterren. 
* `review` verwijst naar de inhoud van de review, de tekst die geschreven is door de consument van Bol.com
* `keywords` zijn verschillende woorden zoals: bezorg, product, service, levering, slecht, goed, nep, misleid. Deze zijn gebruikt om te analyseren hoevaak deze voorkomen (als geheel woord) in de reviews. dit is voor zowel 2019 als 2020 apart gedaan. 
## Gebruik
Er is een Python file (`BP final notebook.ypnb`) met algemene functies. De onderstaande bestanden moeten in de volgende volgorden worden uitgevoerd met Python:
1. `Gemiddelde lengte reviews 2019-2020.py` laat zien wat de gemiddelde lengte van de reviews zijn in tekens. 
2. `Sterrenverdeling_2019-2020.py` laat zien hoe de sterratings per jaar verdeeld zijn. 
3. `Tellen keywords 2019.py` laat zien hoeveel reviews in 2019 over een bepaald keyword gaat. 
4. `Tellen keywords 2020.py`laat zien hoeveel reviews in 2020 over een bepaald keyword gaat. 
5. `Barchart verdeling keywords reviews 2019-2020.py` laat zien hoe de verdeling van keywords in de reviews zijn. 

