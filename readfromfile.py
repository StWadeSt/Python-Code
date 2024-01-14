#Read data from a exteral file
import random

file = open("words.txt", "r")
values = file.read()
list=values.split("\n")
print(list)

