#A simple program using kwargs.
#author: danielCodingGuy

#Kwargs packs all of the arguments into a dictionary.
def hello(**kwargs):
    print("Hello ", end=" ")
    for key,value in kwargs.items(): #Loop will iterate every key value specified in line 10.
        print(value, end=" ")

hello(title="Tech.",first="daniel",middle="Coding",last="Guy")