#The get() function with dictionaries
'''

users = {
  "231": "Stuart",
  "243": "Clint",
  "234": "Ameera",
  "213": "Kedwyn"
}

input = input("Enter the UserId: ")
for i in users:
    if i == n:
        print("Found")
    else:
        print("Not Found")
x = users.get(input, "Invalid USerID")

print( x, "!")
'''


numbers=[23,34,53,56,21,21]


#numbers.discard(25)
try:
  print(numbers[10])
except IndexError:
  print("The index is outside of the list's bounds")