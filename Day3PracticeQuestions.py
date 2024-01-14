#Practice Questions
'''

#Q1
A=[[13,6,4],[5,6,4],[9,8,3]]

d=[2,3,4]

B=[
    [1,3,5],
    [6,7,3],
    [4,9,4]
]

C=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for row in range(len(A)):
    for column in range(len(A[row])):
        C[row][column] = A[row][column] + B[row][column]
        
for z in C:
    print(z)

#Q5

str1 = "Hello there, my name is Stuart. Whats your name?"

list_of_chars=[]
result=''

for letter in str1:
    list_of_chars.append(letter)

for letter in list_of_chars:
    if letter.isalpha() or letter == " ":
        result+= letter.lower()
    else:
        pass

print("Original string:\n"+str1)
print("Altered string:\n"+result)


#Q6

str1 = input("Please enter your sentence: ")

list=[]
for letter in str1:
    if letter.isalpha():
        list.append(letter.lower())
list.sort()
print(list)


#Q8

str1 = "Hello there, my name is Stuart. Whats your name?"
checked_letters=[]
for letter in str1:
    if letter in "aeiou":
        if letter not in checked_letters:
            print(letter, str1.count(letter))
            checked_letters.append(letter)
'''
            
#Q9
users = {
  "231": "Stuart",
  "243": "Clint",
  "234": "Ameera",
  "213": "Kedwyn"
}

new_users={
    "876": "Zuko",
    "761": "Reeves",
    "345": "Maanda"
}

print(users)
users.update(new_users)

print(users)
'''

#Q10
new_users={
    "876": "Zuko",
    "761": "Reeves",
    "345": "Maanda"
}

values= new_users.values()

'''
