# score.py - Berechnet den Score für Trainings
 
def calculate_score(training_type, distance, pulse, speed):
    score_points = 0
    
    # Geschwindigkeit bewerten
    if training_type == "cycling":
        if speed >= 30:
            score_points += 2
        elif speed >= 25:
            score_points += 1
    elif training_type == "running":
        if speed >= 12:
            score_points += 2
        elif speed >= 10:
            score_points += 1
    elif training_type == "swimming":
        if speed >= 3.5:
            score_points += 2
        elif speed >= 2.5:
            score_points += 1
    
    # Puls bewerten
    if training_type == "cycling" and 140 <= pulse <= 160:
        score_points += 2
    elif training_type == "running" and 150 <= pulse <= 170:
        score_points += 2
    elif training_type == "swimming" and 130 <= pulse <= 150:
        score_points += 2
    
    # Score Text zurückgeben
    if score_points >= 3:
        return "Very good performance"
    elif score_points >= 2:
        return "Good performance"
    elif score_points >= 1:
        return "Satisfactory performance"
    else:
        return "Needs improvement"
