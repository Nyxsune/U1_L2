'''
Connor Cox
U1L2
Plot them
'''
from rat import Rat
import breed_rats as BR
import matplotlib.pyplot as plt


def breed():
  generations = 0
  rats = BR.initial_population()
  means = []
  daBiggests = []
  daSmallests = []
  fitness = False
  while fitness == False:
    generations += 1  
    pups = BR.breed(rats)
    pups = BR.mutate(pups)
    mean = BR.calculate_mean(rats)
    fitness = BR.fitness(mean)
    means.append(mean)
    rats, daBiggest, daSmallest = BR.select(rats, pups)
    daBiggests.append(daBiggest)
    daSmallests.append(daSmallest)
    if generations == 500:
      break
  return means, daBiggests, daSmallests

def turnFiles():
  means, daBiggests, daSmallests = breed()
  cycle = [means, daBiggests, daSmallests]
  txtNums = ['', '', '']
  names = ["means.txt", "biggests.txt", "smallests.txt"]
  i = 0
  for listt in cycle:
    for rat in listt:
      txtNums[i] += str(rat)
      txtNums[i] += ", "
    path = names[i]
    with open(path, 'w') as file:
      file.write(txtNums[i])
    i += 1

def main():
  turnFiles()
  files = ["biggests.txt", "means.txt", "smallests.txt"]
  lists = ['', '', '']
  i = 0
  for filee in files:
    path = filee
    with open(path, 'r') as file:
      contents = file.read()
    lists[i] = contents
    i += 1

  h = 0
  for listt in lists:
    lists[h] = listt.split(", ")
    h += 1

  for listt in lists:
    for f in range(len(listt)):
      try:
        listt[f] = int(listt[f])
      except:
        pass
    del listt[-1]

  colors = ["#fb00ff", "#00fbff", "#ffee00"]
  j = 0
  for dataset in lists:
    plt.plot(dataset, color = colors[j])

    plt.title("Rat Growth")
    plt.xlabel("Generation")
    plt.ylabel("Rat Weight (Grams)")

    plt.legend(files)
    plt.savefig('Rat_Graph.png')

    j += 1


if __name__ == "__main__":
  main()
