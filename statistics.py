import math

def calculateStats(numbers):
  if(len(numbers) == 0):
    return {"avg" : math.nan, "max" : math.nan, "min" : math.nan}
  else:
    return{"avg" : sum(numbers)/len(numbers), "max" : max(numbers), "min" : min(numbers)}
emailAlert = 0;
