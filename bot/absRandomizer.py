import numpy as np

workouts = [
        "Bicycles",
        "SMS Leg Tucks",
        "Flutter Kicks",
        "Windshield Wipers",
        "Penguin March",
        "Dead Bugs",
        "Leg Claps",
        "Heels to Heaven",
        "KTE Crunches",
        "Scissor Kicks",
        "Russian V-Up",
        "Side Planks",
        "Toe Touches",
        "Row Boat",
        "Leg Climbers",
        "High-Low Plank",
        "Regular Plank",
        "Moutain Climbers",
        "Boat Hold",
        "Side-Plank Crunch",
]

def getAbWorkout(wildcard):
  workoutString = "Exercise Time: " + str(np.random.choice(["34s", "36s", "38s", "40s"])) + "\n"
  workoutString += "\n".join(np.random.choice(workouts, (11), replace=False)) + "\n"
  workoutString += "Wildcard: " + wildcard
  return workoutString
