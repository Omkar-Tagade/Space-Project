#Date 
from datetime import date
import os




def rocket_parts():
    return "payload, propellant, structure"

def distance_from_earth(destination):
    
    if destination == "Moon":
        return "238,855 miles"
    else:
        return "Unable to compute to that destination"


def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24


def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank} 
    """
    print(output)
    return output

