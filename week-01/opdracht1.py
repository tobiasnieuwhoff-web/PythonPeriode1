# Oefening 1
# Print de volgende zin "Hello World"

print("Hello World!")


# Oefening 2
# Verander de waarde van de onderstaande variabelen.
# Print deze daarna 1 voor 1 uit

naam = "Tobias"
leeftijd = 19
woonstad = "Utrecht"


# Oefening 3
# Gebruik nu bovenstaande variabelen om zinnen te bouwen
# Bijvoorbeeld print("Hallo mijn naam is ", naam) of print(f"Mijn naam is {naam}")

print (f"Mijn naam is {naam}. Ik ben {leeftijd} en woon in {woonstad}")

# Oefening 4
# Maak variabelen aan voor je favoriete game, hoe veel uur je deze hebt gespeeld en welk cijfer je dit spel zou geven
# Print deze daarna in zinnen uit, bijvoorbeeld "Mijn favoriete game is Minecraft" "Ik heb deze game 150 uur gespeeld", "Ik geef deze game een 8.5"

game = "Battlefield 1"
uur = 500
cijfer = 10

print (f"Mijn favoriete game is {game}, ik heb er {uur} uur in en geef het een {cijfer}")


# Oefening 5
# Maak twee variabelen aan, number1 en number2
# Bereken daarna de som (+), het verschil (-) en het product (*) uit van deze nummers.
# Print daarna de uitkomsten uit

number1 = 10
number2 = 20
plus = number1 + number2
verschil = number2 - number1

print(plus, verschil)

# Oefening 6
# Maak een simpel game character met minimaal de volgende variabelen: name, health, level, damage
# Print deze vervolgens uit
# Zorg er daarna voor dat je character 20 damage neemt, print nu de nieuwe waarde van zijn health uit

naam = "Tobias"
health = 25
level = 40
damage = 15
print(naam)
print(health)
print(level)
print(damage)
health -= 20
print(health)

# Oefening 7
# Ga verder met je character van de vorige oefening. Voeg nu een nieuw variabel "weapon" toe.
# Geef het wapen een naam, verhoog de damage van je character en verhoog het level met 1
# Print daarna de nieuwe waardes uit 

weaponmaam = "Longsword"
weapon = 15
damage += weapon

level += 1

print(naam)
print(health)
print(level)
print(damage)

# Oefening 8
# Maak een programma dat een profiel van een gamer laat zien
# Maak minimaal de volgende variabelen: name, age, favouriteGame, hoursPlayed, level, score
# Print al deze informatie netjes uit
# Verhoog daarna de score van het profiel met 250 en print de nieuwe waarde
# Bonus! Voeg zelf 3 nieuwe variabelen toe

name = "Tobias"
age = 19
favoriteGame = "Legend of Zelda Majora's Mask"
hoursPlayed = 320
level = 110
score = 1400

print(f"Name = {name}")
print(f"Age = {age}")
print(f"FavoriteGame = {favoriteGame}")
print(f"HoursPlayed = {hoursPlayed}")
print(f"Level = {level}")
print(f"Score = {score}")
score += 250
print(score)

#git push -u origin week-01