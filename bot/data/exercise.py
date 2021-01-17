class TimedExercise: 
  name = 'workout'
  lengthSeconds = 0
  restSeconds = 0

  def __init__(self, name, lengthSeconds, restSeconds):
    self.name = name
    self.lengthSeconds = lengthSeconds
    self.restSeconds = restSeconds
  
  def getLength(self):
    return self.lengthSeconds

  def getName(self): 
    return self.name

  def getRest(self):
    return self.restSeconds

  