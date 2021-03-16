from random import shuffle
import random

randomlist = [] #if u want using str value, u can add here
for i in range(0,100):
    n = random.randint(25,50) #random using number
    randomlist.append(str(n))
target = "2000"

#open text
with open('Fullprofile.txt', 'r') as file :
  filedata = file.read()
  shuffle(randomlist)
  for x in range(len(filedata)):
       for ele in randomlist:
            # replacing item
           filedata = filedata.replace(target, ele, 1)
  #

# Write the file out again
with open('Fullprofile_new.txt', 'w') as file:
  file.write(filedata)

