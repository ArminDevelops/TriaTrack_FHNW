import csv
from TRIA.score import *
from TRIA.complete_stats import *
from TRIA.load_training import *
from TRIA.add_training import *
from TRIA.display_stats import *

WORKOUTS = ["swimming", "cycling", "running"]
MAIN_MENU = ["Show stats", "Add new Training", "End Program"]


def print_main_menu():
    i = 1
    print("\nWelcome to TriaTrack, your tracker for all your triathletic workouts")
    print("-" * 70)
    for menu_point in MAIN_MENU:
        print(f"{i}) {menu_point}")
        i += 1
    print("-" * 70)


def main():
    main_menu_logic()


def main_menu_logic():

    while True:
        print_main_menu()
        try:
            choice_menu = int(input("Choose function: "))
        except ValueError:
            print("Please enter a number.")
            print("-" * 70)
            continue
        if choice_menu == 1:
            stats_menu_logic()
        elif choice_menu == 2:
            new_training_menu_logic()
        elif choice_menu == 3:
            break
        else:
            print("Invalid choice")
            print("-" * 70)
    print("Goodbye see you next time")



main()
