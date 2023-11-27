#A simple program using *args.
#author: danielCodingGuy

#Args will pack all arguments into a tuple.
def add(*stuff): #Instead of adding all of the arguments specified in line 13 we just use *stuff to save ourselfes a headache.
    sum = 0
    stuff = list(stuff) #Casted tuple as list.
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8,9))