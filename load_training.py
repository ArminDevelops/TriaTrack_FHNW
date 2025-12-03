from TRIA.display_stats import *
import csv


def load_training(workout_type, time_span):
    total_distance = 0.0
    sum_pulse = 0.0
    sum_speed = 0.0
    counter = 0


    try:
        with open("trainings.csv", "r", newline='') as file:
            reader = csv.reader(file)
            print("Reading training data...")

            for row in reader:
                if counter >= time_span:
                    break

                if len(row) != 5:
                    continue

                try:
                    discipline = row[0]
                    distance = float(row[1])
                    time_val = float(row[2])
                    pulse = float(row[3])
                    avg_speed = float(row[4])
                except (ValueError, IndexError):
                    continue

                # Check if we want all workouts or specific type
                if workout_type == "all" or discipline == workout_type:
                    total_distance += distance
                    sum_pulse += pulse
                    sum_speed += avg_speed
                    counter += 1

    except FileNotFoundError:
        print("No trainings file found.")
        print("-" * 70)
        input("Press Enter to continue...")
        return
    except IOError as e:
        print(f"Error while loading: {e}")
        print("-" * 70)
        input("Press Enter to continue...")
        return

    display_training_stats(workout_type, counter, total_distance, sum_pulse, sum_speed)
