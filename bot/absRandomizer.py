import numpy as np

workouts = [
        "Bicycles", 
        "Side-middle-side Leg Tucks", 
        "Flutter Kick", 
        "Windshield Wipers",
        "Penguin March",
        "Dead Bugs",
        "Leg Claps",
        "Heels to Heaven",
        "KTE Crunche",
        "Scissor Kicks",
        "Russian V-Up",
        "Side Plank (30 each side)",
        "Toe Touches",
        "Row Boats",
        "Leg Climbers"
]

def getAbWorkout(wildcard):
  randomizedWorkout = "\n".join(np.random.choice(workouts, (11), replace=False))
  randomizedWorkout += "\n" + wildcard
  return randomizedWorkout
