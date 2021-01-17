import numpy as np
from data.exercise import TimedExercise 
import math

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

lengths = [
  34,
  36,
  38,
  40
]

numExercises = 11

def getAbWorkout(wildcard):
  workoutTime = np.random.choice(lengths)
  workoutStringList = np.random.choice(workouts, (numExercises), replace=False)

  workoutList = [TimedExercise(workoutName, workoutTime, workoutTime) for workoutName in workoutStringList]
  workoutList.insert(math.ceil(numExercises/2), TimedExercise("Rest", 0, workoutTime))
  workoutList.append(TimedExercise(wildcard, workoutTime, workoutTime))

  return workoutList
  
def getAbWorkoutStringFromWorkoutList(workoutList):
  workoutString = "Exercise Time: " + str(workoutList[0].getLength()) + "\n"
  workoutString += "\n".join([workout.getName() for workout in workoutList[:-1]]) + "\n"
  workoutString += "Wildcard: " + workoutList[-1].getName()
  return workoutString
