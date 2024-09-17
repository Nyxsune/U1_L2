'''
Connor Cox
U1L1
Chunky Rat Borl (Boy Girl)
'''
from rat import Rat
import breed_rats as BR
import time

def breed():
  generations = 0
  rats = BR.initial_population()
  means = []
  daBiggest = 0
  fitness = False
  speed = time.time() 
  while fitness == False:
    generations += 1  
    pups = BR.breed(rats)
    pups = BR.mutate(pups)
    mean = BR.calculate_mean(rats)
    fitness = BR.fitness(mean)
    means.append(mean)
    rats, daBiggest = BR.select(rats, pups)
    if generations == 500:
      break
  newSpeed = time.time()
  speed = newSpeed - speed
  return generations, means, daBiggest, speed, mean

def prettyMeans(means):
  meanss = ''
  for mean in means:
    meanss += str(mean)
    meanss += " "
  
  return meanss

def main():
  generations, means, daBiggest, speed, finalMean = breed()
  means = prettyMeans(means)
  print(f"""
  ~~~~~~~~~~~~Results~~~~~~~~~~~~

  Final Population Mean: {finalMean}

  Generations: {generations}
  Experiment Duration: {int(generations / 10)} years
  Simulation Duration: {speed} seconds

  Da Biggest Boy/Girl:
  {daBiggest}

  Generation Weight Averages (grams)

  {means}
  """)

if __name__ == "__main__":
  main()