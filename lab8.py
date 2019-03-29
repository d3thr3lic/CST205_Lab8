def pickAndExplore():
  clip = makeSound(pickAFile())
  #play(clip)
  #decreaseVolume(clip)
  #changeVolume(clip, 2)
  #print maxSample(clip)
  #clip = maxVolume(clip)
  goToEleven(clip)
  explore(clip)

def maxVolume(sound):
  maxPossibleSampleValue = 127
  largest = maxSample(sound)
  factor = float(maxPossibleSampleValue)/largest
  print maxPossibleSampleValue
  print largest
  print factor
  for sample in getSamples(sound):
    currentValue = getSampleValue(sample)
    setSampleValue(sample, currentValue * factor)
  return sound
  
def goToEleven(sound):
  maxPossibleSampleValue = 127
  for sample in getSamples(sound):
    if getSampleValue(sample) > 0:
      setSampleValue(sample, maxPossibleSampleValue)
    else:
      setSampleValue(sample, maxPossibleSampleValue * -1)

def maxSample(sound):
  runningMax = 0;
  for sample in getSamples(sound):
    localMax = max(getSampleValue(sample), runningMax)
    if localMax > runningMax:
      runningMax = localMax
  return runningMax
  
def printSample():
  clip = makeSound(pickAFile())
  #sample = getSamples(clip)
  print getSampleValueAt(clip, 10000)

def decreaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value / 2)
      
def changeVolume(sound, factor):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * factor)

#from lab8 instructions
def increaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * 2)