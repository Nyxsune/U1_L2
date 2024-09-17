from rat import Rat
from random import triangular
from random import randint
from random import uniform
from numpy.random import choice

# Global Variables

GOAL = 50000                # Target average weight (grams)
NUM_RATS = 20               # Max adult rats in the lab
INITIAL_MIN_WT = 200        # The smallest rat (grams)
INITIAL_MAX_WT = 600        # The chonkiest rat (grams)
INITIAL_MODE_WT = 300       # The most common weight (grams)
MUTATE_ODDS = 0.01          # Liklihood of a mutation
MUTATE_MIN = 0.5            # Scalar mutation - least beneficial
MUTATE_MAX = 1.2            # Scalar mutation - most beneficial
LITTER_SIZE = 8             # Pups per litter (1 mating pair)
GENERATIONS_PER_YEAR = 10   # How many generations are created each year
GENERATION_LIMIT = 500      # Generational cutoff - stop breeded no matter what

# maths

def calculate_weight(sex, mother, father):
  min = Rat.getWeight(mother)
  max = Rat.getWeight(father)

  if sex == "M":
    wt = int(triangular(min, max, max))
  else:
    wt = int(triangular(min, max, min))
  return wt

# Initial rats

def initial_population():
  rats = [[],[]]
  mother = Rat("F", INITIAL_MIN_WT)
  father = Rat("M", INITIAL_MAX_WT)
  
  for r in range(NUM_RATS):
    if r < 10:
      sex = "M"
      ind = 0
    else:
      sex = "F"
      ind = 1
  
    wt = calculate_weight(sex, mother, father)
    R = Rat(sex, wt)
    rats[ind].append(R)
  
  return rats

def breed(rats):
  pups = [[],[]]
  pairs = []
  for i in range(10):
    pair = [rats[0][i], rats[1][i]]
    pairs.append(pair)
  for pair in pairs:
    for i in range(LITTER_SIZE):
      sex = randint(1,100)
      if sex % 2 == 0:
        sex = "F"
        ind = 0
      elif sex % 2 == 1:
        sex = "M"
        ind = 1
      wt = calculate_weight(sex, pair[1], pair[0])
      R = Rat(sex, wt)
      pups[ind].append(R)
  return pups

def mutate(pups):
  for sex in pups:
    for pup in sex:
      list = [0, 1]
      random = choice(list, 1, p=[MUTATE_ODDS, (1-MUTATE_ODDS)])
      if random == 0:
        mutation = uniform(MUTATE_MIN, MUTATE_MAX)
        new_wt = int(pup.getWeight() * mutation)
        pup.setWeight(new_wt)
  
  return pups

def select(rats, pups):
  best = [[], []]
  daBiggest = pups[0][0]
  daSmallest = pups[0][1]
  total = [[], []]
  for i in range(2):
    for pup in pups[i]:
      total[i].append(pup)
  for i in range(2):
    for rat in rats[i]:
      total[i].append(rat)
  
  for i in range(2):
    for j in range(10):
      biggest = total[i][0]
      for pup in total[i]:
        if pup.litters < 5:
          pup.litters += 1
          if pup > biggest:
            biggest = pup
          if pup > daBiggest:
            daBiggest = pup
          if pup < daSmallest:
            daSmallest = pup
      index = total[i].index(biggest)
      total[i].pop(index)
      best[i].append(biggest)

  return best, daBiggest, daSmallest
'''
def select(rats, pups):
  rats = [[],[]]
  daBiggest = pups[0][0]
  for i in range(2):
    for j in range(10):
      biggest = pups[i][0]
      for pup in pups[i]:
        if pup.litters < 5:
          pup.litters += 1
          if pup > biggest:
            biggest = pup
          if pup > daBiggest:
            daBiggest = pup
      index = pups[i].index(biggest)
      pups[i].pop(index)
      rats[i].append(biggest)
  
  return rats, daBiggest
'''  

def calculate_mean(rats):
  sumWt = 0
  numRats = 0
  for sex in rats:
    for rat in sex:
      numRats += 1
      sumWt += rat.weight

  return sumWt // numRats

def fitness(mean):
  return mean >= GOAL

def main():
  rats = initial_population()
  pups = breed(rats)
  pups = mutate(pups)
  select(rats, pups)
  mean = calculate_mean(rats)
  #fitness = fitness(mean)

if __name__ == "__main__":
  main()
