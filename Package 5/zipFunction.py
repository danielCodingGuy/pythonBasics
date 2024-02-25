# Simple program that creates zip object stored in tuples.
# author: danielCodingGuy

usernames = ["daniel","Coding","Guy"]
passwords = ["p@ssword","pass123","abcdef123"]

users = dict(zip(usernames, passwords)) # Program will print usernames and passwords in dictionary.

print(type(users))

for key,value in users.items():
    print(key + " : " + value)