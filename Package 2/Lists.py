#Simple program using lists.
#author: danielCodingGuy

food = ["pizza","hamburger","hotdog","spaghetti","pudding"] #Thats how you declare a list.

food[1] = "sushi" #Updates list and changes the value on index 1(hamburger) with sushi.

print(food[0]) #Prints only index 0 from the list - sushi.

food.append("ice cream") #Adds ice cream on the last index of the list.
food.remove("hotdog") #Removes hotdog from the list.
food.pop() #Removes the element on the last index in the list.
food.insert(0,"cake") #Inserts cake on the first index in the list, and moves other elements one idex further.
food.sort() #Sorts the list alphabetically.
food.clear() #Removes everything from the list

for x in food:
    print(x)