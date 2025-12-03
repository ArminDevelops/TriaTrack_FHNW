from TRIA.score import *

def display_training_stats(workout_type, counter, total_distance, sum_pulse, sum_speed):
    if counter > 0:
        workout_display = "all" if workout_type == "all" else workout_type
        avg_pulse = sum_pulse / counter
        avg_speed = sum_speed / counter
        
        # Score berechnen basierend auf Durchschnittswerten
        score = calculate_score(workout_type, total_distance, avg_pulse, avg_speed)

        print(f"\nDisplaying your stats for the last {counter} {workout_display}-training(s)")
        print("-" * 70)
        print(f"Total distance: {total_distance:.2f} KM")
        print(f"Average pulse: {avg_pulse:.2f} Beats per Minute")
        print(f"Average speed: {avg_speed:.2f} KM/H")
        print(f"Performance Score: {score}")
    else:
        print(f"\nNo {workout_type} trainings found.")

    print("-" * 70)
    input("Press Enter to continue...")
