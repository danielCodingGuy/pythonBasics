#A simple program using tuples.
#author: danielCodingGuy

student = ("Daniel",20,"male") #Thats how we create tuple.

print(student.count("Daniel")) #This function prints every "Daniel" that appears in our tuple.
print(student.index("male")) #This function prints index number where "male" appears in our tuple.

for x in student: #This for loop will print every value in student tuple.
    print(x)

if "Daniel" in student: #If there is value "Daniel" tuple program will print "Daniel is here!".
    print("Daniel is here!") 