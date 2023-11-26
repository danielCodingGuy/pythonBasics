#A simple program that uses string slicing.
#author: danielCodingGuy

name = "Daniel CodingGuy"

first_name = name[:6] #Creating substring which value will be only first name [start:stop:step].
last_name = name[7:] #You can leave the stop blank, program will start on index 6 and go till the end of the string.
nickname = name[::4] #Steps in this situation will write every fourth letter from the name.
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(nickname)
print(reversed_name)

website1 = "http://github.com"
website2 = "http://microsoft.com"

slice = slice(7,-4) #Creating slice which starts at index 7 and ends 4 indexes before the last index

print(website1[slice])
print(website2[slice]) #You can reuse the slice on different strings