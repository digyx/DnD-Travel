from typing import List
from random import randint
from subprocess import run

def determine_party_speed() -> int:
    print("How fast is the party traveling?")
    print("\t1. Slow")
    print("\t2. Medium")
    print("\t3. Fast")
    return int(input())


def get_danger_level() -> int:
    print("What is the danger level of the area?")
    print("\t1. Civilized/Well Traveled")
    print("\t2. Dangerous Frontier")
    print("\t3. Enemy Territory")
    print("\t4. Regularly Patrolled Enemy Territory")
    print("\t5. They are Being Hunted")
    return int(input())


def log_party_speed(travel_speel: int):
    map = [
        "2/3",
        "1",
        "4/3"
    ]

    other_map = [
        "Advantage, normal Foraging",
        "Normal, disadvantage Foraging",
        "Diadvantage, no Foraging",
    ]

    print("Days of Travel: {} day(s)".format(map[travel_speed - 1]))
    print("Modifiers: {}\n".format(other_map[travel_speed - 1]))


def generate_encounter_order(danger_level: int):
    base = [1,2,3,4,5,6]
    final = []
    times_of_day = [
        "Morning",
        "Afternoon",
        "Evening",
        "Dusk",
        "Midnight",
        "Predawn"
    ]

    for _ in range(6):
        index = randint(0, len(base) - 1)
        final.append(base.pop(index))

    print("Encounters:")
    for i in range(danger_level):
        index = final[i] - 1
        print("\t{}".format(times_of_day[index]))
    
    print("\nDiscovery: {}".format(times_of_day[final[danger_level] - 1]))



if __name__ == "__main__":
    # Beginning of the Day
    travel_speed = determine_party_speed()
    run("clear")

    danger_level = get_danger_level()
    run("clear")

    log_party_speed(travel_speed)
    generate_encounter_order(danger_level)
