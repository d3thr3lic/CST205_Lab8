###CST205 -- Lab8
#Mitchell Saunders
#Nicholas Saunders

def pickAndExplore():
  clip = makeSound(pickAFile())
  ###Uncomment any of the functions below
  ###to use any function.
  
  #play(clip) # no modifications
  
  #maxVolume(clip)
  #decreaseVolume(clip)
  #changeVolume(clip, 2)
  #print maxSample(clip)
  #maxVolume(clip)
  #goToEleven(clip)
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

#takes sample values from source, and sets sampleValues to max or min.     
def goToEleven(sound):
  maxPossibleSampleValue = 127
  for sample in getSamples(sound):
    if getSampleValue(sample) > 0:
      setSampleValue(sample, maxPossibleSampleValue)
    else:
      setSampleValue(sample, maxPossibleSampleValue * -1)

#sets sound to max sound sample value.
def maxSample(sound):
  runningMax = 0;
  for sample in getSamples(sound):
    localMax = max(getSampleValue(sample), runningMax)
    if localMax > runningMax:
      runningMax = localMax
  return runningMax

#if called, will print to value of the sample of a clip    
def printSample():
  clip = makeSound(pickAFile())
  #sample = getSamples(clip)
  print getSampleValueAt(clip, 10000)

#decreases volume of sound by half
def decreaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value / 2)

#like decreaseVolume, but it modifable by a factor parameter.            
def changeVolume(sound, factor):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * factor)

#from lab8 instructions
def increaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * 2)