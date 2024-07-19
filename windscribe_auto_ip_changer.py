# You can Chnage The (timetowait) To Set A Custom Time In Minutes
# If A Server Is Down OR Not Found The Script Will Wait Another (timetowait) Minutes For The Next Location


import os
import time
import random
from datetime import datetime

timetowait = 5

currenttime = datetime.now()
regions = ["Tirana - Besa", "Buenos Aires - Tango", "Adelaide - Lofty", "Adelaide - Oval", "Brisbane - Bad Koala", "Brisbane - Good Koala", "Melbourne - Port Phillip", "Melbourne - Yarra", "Perth - Herdsman", "Perth - Kings Park", "Sydney - Opera House", "Sydney - Squidney", "Vienna - Boltzmann", "Vienna - Hofburg", "Brussels - Guildhouse", "Novi Travnik - Pisanica", "Sarajevo - Burek", "Sao Paulo - Mercadao", "Sao Paulo - Pinacoteca", "Sofia - Nevski", "Phnom Penh - Botum Pagoda", "Halifax - Crosby", "Montreal - Bagel Poutine", "Montreal - Expo 67", "Toronto - Comfort Zone", "Toronto - The 6", "Vancouver - Granville", "Vancouver - Stanley", "Vancouver - Vansterdam", "Santiago - Cueca", "Bogota - Rololandia", "Zagreb - Tkalciceva", "Nicosia - Blue Lagoon", "Prague - Staromak", "Prague - Vltava", "Copenhagen - LEGO", "Quito - Cuy", "Tallinn - Lennujaam", "Troll - Station", "Helsinki - Sauna", "Helsinki - Tram", "Marseille - La Marseillaise", "Paris - Jardin", "Paris - Seine", "Tbilisi - Ghvino", "Frankfurt - Castle", "Frankfurt - Wurstchen", "Accra - Best Jollof", "Athens - Agora", "Athens - Odeon", "Hong Kong - Phooey", "Hong Kong - Victoria", "Budapest - Danube", "Reykjavik - Fuzzy Pony", "Reykjavik - Reyka", "Mumbai - Mahim", "New Delhi - Chole Bhature", "Jakarta - Ancol", "Jakarta - Old Town", "Dublin - Dullahan", "Dublin - Grafton", "Dublin - Guinness", "Ashdod - Yam Park", "Milan - Duomo", "Milan - Galleria", "Rome - Colosseum", "Tokyo - Shinkansen", "Tokyo - Wabi-sabi", "Nairobi - Sigiria", "Riga - Daugava", "Riga - Saeima", "Vilnius - Neris", "Luxembourg - Chemin", "Kuala Lumpur - Perdana", "Querétaro - Wey", "Chisinau - Dendrarium", "Amsterdam - Bicycle", "Amsterdam - Canal", "Amsterdam - Red Light", "Amsterdam - Tulip", "Auckland - Hauraki", "Auckland - Parnell", "Skopje - Vardar", "Oslo - Fjord", "Panama City - Papers", "Lima - Amaru", "Manila - Pasig", "Gdansk - Motlawa", "Warsaw - Curie", "Warsaw - Vistula", "Lisbon - Bairro", "Bucharest - No Vampires", "Moscow - Goodbye Lenin", "Saint Petersburg - Hermitage", "Saint Petersburg - Shnur", "Belgrade - Rakia", "Singapore - Garden", "Singapore - Marina Bay", "Singapore - SMRT", "Bratislava - Devin Castle", "Johannesburg - District", "Johannesburg - Lindfield", "Johannesburg - Springbok", "Seoul - Han River", "Seoul - Hangang", "Barcelona - Batllo", "Madrid - Prado", "Stockholm - Djurgarden", "Stockholm - Ikea", "Stockholm - Syndrome", "Zurich - Alphorn", "Zurich - Altstadt", "Zurich - Lindenhof", "Taipei - Datong", "Bangkok - Hangover", "Bangkok - Lumphini", "Istanbul - Galata", "Istanbul - Lygos", "Kyiv - Ghost", "Dubai - Khalifa", "Edinburgh - Keeper Willie", "London - Biscuits", "London - Crumpets", "London - Custard", "Manchester - United", "Atlanta - Mountain", "Atlanta - Piedmont", "Dallas - Ammo", "Dallas - BBQ", "Dallas - Ranch", "Dallas - Trinity", "Denver - Barley", "Kansas City - Glinda", "Boston - Harvard", "Boston - MIT", "Buffalo - Bill", "Charlotte - Earnhardt", "Chicago - Cub", "Chicago - The L", "Chicago - Wrigley", "Cleveland - Brown", "Detroit - Coney Dog", "Miami - Florida Man", "Miami - Snow", "Miami - Vice", "New Jersey - Situation", "New York - Empire", "New York - Grand Central", "New York - Insomnia", "Orlando - Tofu Driver", "Philadelphia - Fresh Prince", "Philadelphia - Sunny", "South Bend - Hawkins", "Tampa - Cuban Sandwich", "Washington DC - Precedent", "Bend - Oregon Trail", "Las Vegas - Casino", "Los Angeles - Cube", "Los Angeles - Dogg", "Los Angeles - Eazy", "Los Angeles - Lamar", "Los Angeles - Pac", "Phoenix - Floatie", "San Francisco - Sanitation", "San Jose - Santana", "Santa Clara - Inside", "Seattle - Cobain", "Seattle - Cornell", "Seattle - Hendrix", "Hanoi - Red River", "Toronto - Mansbridge", "Tokyo - Kaiju", "London - The Tube", "New York - Radiohall"] # define locations here

print("Windscribe Auto IP Changer")
print("Starting..")

while True:
    print("-----------------------------------------")
    print("Rotating IP Now")
    randregion = random.choice(regions)
    print(randregion)
    os.system("windscribe-cli connect " + str(randregion))
    print("Connected at " + str(currenttime))
    print("Waiting " + str(timetowait) + " Minutes")
    print("--------------------sex---------------------")
    time.sleep(int(timetowait) * 60)

    
