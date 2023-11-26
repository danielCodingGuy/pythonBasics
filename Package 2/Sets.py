#Simple program using sets.
#author: danielCodingGuy


#Set is unordered, unindexed and does not include duplicate values.

utensils = {"fork","spoon","knife"} #Thats how you declare a set.
dishes = {"bowl","plate","cup"}

utensils.add("napkin") #This function adds something to set.
utensils.remove("fork") #This function removes something from the set, in this example "fork".
utensils.clear() #This function is clearing set.
utensils.update(dishes) #Adds set to set, in this example adds dishes to utensils.

dinner_table = utensils.union(dishes) #Creates set with merged two sets - utensils and dishes.

print(utensils.difference(dishes)) #This function prints what one set has that other set does not have.
print(utensils.intersection(dishes)) #This function will print whatever the two mentioned sets have in common.

for x in dinner_table:
    print(x)