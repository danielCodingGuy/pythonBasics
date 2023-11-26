#Simple program that is using type casts.
#author: danielCodingGuy

x = 1   #int
y = 2.0 #float
z = "3" #string

y = int(y) #casted float to int changing 2.0 to 2.
z = int(z) #casted string from float to int.
x = float(x) #casted x to float changing it from 1 to 1.0.

print("X is " + str(x))
print("Y is " + str(y))
print("Z is " + str(z))