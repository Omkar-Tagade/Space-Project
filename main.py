import space as sp
from datetime import date
import os


def main():

    # print(os.listdir())
    print("\n\nDate : ", date.today())
    print("-------------------------------------------------------")
    sp.generate_report(80, 70, 75)

    #Conversion between light years and parsecs
    parsecs_input = input("Input number of parsecs: --- ")
    parsecs = int(parsecs_input)
    lightyears = 3.26156 * parsecs

    print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")

    #Use of if and else
    object_size = int(input("Input Size of object in mm: --- "))
    if object_size > 5:
        print('We need to keep an eye on this object')
    else:
        print('Object poses no threat.')

    #Informatin about the Moon
    text = """Interesting facts about the Moon. \
        The Moon is Earth's only satellite. \
        There are several interesting facts about the Moon and how it affects life here on Earth.\
        On average, the Moon moves 4cm away from the Earth every year. \
        This yearly drift is not significant enough to cause immediate effects on Earth. \
        The highest daylight temperature of the Moon is 127 C."""

    sentences = text.split('. ')
    print(sentences)

    #Distance between two planets in km and miles
    first_planet = int(input("Distance of the first planet from the Sun in km: --- "))
    second_planet = int(input("Distance of the second planet from the Sun in km: --- "))

    distance_km = second_planet - first_planet
    print(distance_km)

    distance_mi = distance_km / 1.609344
    print(distance_mi)

    #List of planets
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    print(planets)

    planets.append("Pluto")

    print("Actually, there are", len(planets), "planets")

    print(planets[-1], "is the last planet")

    user_planet = input("Please enter the name of the planet (with a capital letter to start): >>> ")

    planet_index = planets.index(user_planet)
    print("Here are the planets closer than " + user_planet)
    print(planets[0:planet_index])

    new_planet = ''

    while new_planet.lower() != 'done':
        new_planet = input('Enter a new planet or done if done: >>> ')
        if new_planet:
            planets.append(new_planet)

        for planet in planets:
            print(planet)


    planet = {'name': 'Mars','moons': 2}
    print(f'{planet["name"]} has {planet["moons"]} moon(s)') 

    planet['circumference (km)'] = {'polar': 6752,'equatorial': 6792}
    print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')

    planet_moons = {'mercury': 0,'venus': 0,'earth': 1,'mars': 2,'jupiter': 79,'saturn': 82,'uranus': 27,'neptune': 14,'pluto': 5,'haumea': 2,'makemake': 1,'eris': 1}

    moons = planet_moons.values()
    total_planets = len(planet_moons.keys())

    total_moons = 0
    for moon in moons: #such type of loop is called foreach loop or enhanced for loop
        total_moons = total_moons + moon

    average = total_moons / total_planets

    print(f'Each planet has an average of {average} moons')

    destination=input("Name of destination: >>> ")
    print("Distance : ", sp.distance_from_earth(destination))

    print("Days To Complete : ",round(sp.days_to_complete(238855, 75)))

    print("The rocket parts are : ", sp.rocket_parts())


main()