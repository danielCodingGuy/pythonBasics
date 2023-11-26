#A simple program using control statements.
#author: danielCodingGuy

# break - ending loop entirely.
# continue - skips to the next iteration of the loop.
# pass - placeholder.

while True: #Loop that will execute till the requriements are met.
    name = input("Enter your name: ") 
    if name!= "": #If the name is not blank then break.
        break

phone_number = "123-456-789"

for i in phone_number:
    if i == "-": #If there is a dash.
        continue #Skip the dashes.
    print(i, end="") #Added end="" to avoid printing every number in seperate line.

for i in range(1,21):
    if i == 13: #If number is 13.
        pass #Pass the number.
    else:
        print(i)