from random import shuffle
import random

randomlist = [] #if u want using str/text value, u can add here
for i in range(0,100):
    n = random.randint(25,50) #using random number for replacing
    randomlist.append(str(n))
target = "2000" #text what u want change

#open text
with open('Yourfile.txt', 'r') as file :
  filedata = file.read()
  shuffle(randomlist)
  for x in range(len(filedata)):
       for ele in randomlist:
            # replacing item
           filedata = filedata.replace(target, ele, 1)
  #

# Write the file out again
with open('Yourfile_new.txt', 'w') as file:
  file.write(filedata)

