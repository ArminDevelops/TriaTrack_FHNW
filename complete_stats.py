from TRIA.load_training import *
from TRIA.score import *
WORKOUTS = ["swimming", "cycling", "running"]



def print_stats_menu():
    i = 1
    print("\nWhich Stats would you like to show?")
    print("-" * 70)
    for workout in WORKOUTS:
        print(f"{i}) Show {workout} workouts")
        i += 1
    print(f"{i}) Show all workouts")
    print("-" * 70)


def stats_menu_logic():
    print_stats_menu()

    while True:
        try:
            choice_stats = int(input("Which Stats would you like to show?: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if 1 <= choice_stats <= len(WORKOUTS):
            idx = choice_stats - 1
            print("-" * 70)
            print_stats_menu_time_span()
            stats_menu_timespan_logic(WORKOUTS[idx])
            break
        elif choice_stats == len(WORKOUTS) + 1:
            print("-" * 70)
            print_stats_menu_time_span()
            stats_menu_timespan_logic("all")
            break
        else:
            print("Invalid input")


def print_stats_menu_time_span():
    print("\nWorkout Analyser")
    print("-" * 70)


def stats_menu_timespan_logic(workout_type):
    while True:
        try:
            time_span = int(input("How many of your workouts would you like to analyse: "))


            if time_span > 0:
                load_training(workout_type, time_span)
                break
            else:
                print("Invalid input")
        except ValueError:
            print("Please enter a number.")

def display_training_stats(workout_type, counter, total_distance, sum_pulse, sum_speed):
    if counter > 0:
        workout_display = "all" if workout_type == "all" else workout_type
        avg_pulse = sum_pulse / counter
        avg_speed = sum_speed / counter

        score = calculate_score(workout_type, total_distance, avg_pulse, avg_speed)

        print(f"\nDisplaying your stats for the last {counter} {workout_display}-training(s)")
        print("-" * 70)
        print(f"Total distance: {total_distance:.2f} KM")
        print(f"Average pulse: {avg_pulse:.2f} Beats per Minute")
        print(f"Average speed: {avg_speed:.2f} KM/H")
        print(f'Performance score: {score}')
    else:
        print(f"\nNo {workout_type} trainings found.")
        
    print("-" * 70)
    input("Press Enter to continue...")
