#A simple program using dictionaries in python.
#author: danielCodingGuy

capitals = {'USA':'Washington DC', #Thats how you declare dictionary.
            'Poland':'Warsaw',
            'Spain':'Madrid',
            'Japan':'Tokyo'}

capitals.update({'Norway':'Oslo'}) #This function will add record Norway, Oslo to our dictionary.
capitals.update({'Poland':'Gdańsk'}) #This function will change value assigned to Poland from Warsaw to Gdańsk.
capitals.pop('Japan') #This function will remove Japan from our dictionary.

print(capitals['Poland']) #This function prints value assigned to Poland.
print(capitals.get('Norway')) #This function checks if we have key value Norway assigned to our dictionary.
print(capitals.keys()) #This function will print only the keys, without values from our dictionary.
print(capitals.values()) #This function will print only the values from our dictionary.
print(capitals.items()) #This function will print entire dictionary.

for key,value in capitals.items(): #For each key value in dictionary this function will print redord our dictionary.
    print(key,value)

capitals.clear() #This function will clear our dictionary.