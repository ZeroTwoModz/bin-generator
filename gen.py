import random
import os
import time
from os import system, name
os.system('cls' if name == 'nt' else 'clear')
save = open(f"{os.getcwd()}\\bins.txt", 'a')
howmuch = input("How much bin do you want?\n")
x = int(howmuch)
print("Started")
for i in range(x):
    w = random.randint(410000,520000)
    w = str(w)
    w = w + "\n"
    save.write(w)
    save.flush()
print("Done, I've saved bins in 'bins.txt'")
