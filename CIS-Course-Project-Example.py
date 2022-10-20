print("Hello class!")
print("\nThis is an example of how to make a story using user inputs to create their own adventure")
print("\nI am going to ask you a few questions....please be sure to press enter after your submissions")

color = input("\nWhat is your favorite color?:    ")
while len(color) == 0:
    color = input("\nWhat is your favorite color?:    ")

number = input("\nWhat is your favorite number?:   ")
while len(number) == 0:
    number = input("\nWhat is your favorite number?:   ")

name = input("\nWhat is your friends' name?:   ")
while len(name) == 0:
    name = input("\nWhat is your friends' name?:   ")

coast = input("\nWhat coast do you live near? East or West:    ")
while len(coast) == 0:
    coast = input("\nWhat coast do you live near? East or West:    ")

print("\nLets begin")

print("\nThere once was a young boy who had the favorite color of " + color + ".")
print("\nThis was his favorite color because it consisted of " + number + " letters.")

favoriteCoast = input("\nShould the young boy visit his favorite " + coast + " coast ?" ", enter yes or no   ")
if favoriteCoast == "yes":
    print("\nThe young boy was able to meet his family and friends, but most importantly " + name + " was also there.")

    print("\nNow that the young boy has made to the " + coast + " he is trying to decide if he should go back home.")
    home = input("\nShould the young boy go home? Please enter yes or no?  ")
    if home == "yes":
        print("\nHe returns home and realizes he needs to complete the rest of his labs in his college class.")

    else:
        print("\nThe young man understands that he will have to retake the class next semester.")

else:
    print("\nThe young boy was sad and unable to see his favorite friend " + name + " this time.")
    print("\nNow that the young boy was sad he was trying to find some that would cheer him up.")
    cheerUp = input("\nAs the young man is trying to cheer himself up...what should he do? get ice cream or a burger? ")
    while cheerUp.lower() != "get ice cream" and cheerUp.lower() != "burger":
        cheerUp = input("\nAs the young man is trying to cheer himself up...what should he do? get ice cream or a burger? ")
    if cheerUp == "get ice cream":
        print("\nThe young man stops at cold stone and enjoys fresh ice cream.")
    elif cheerUp == "burger":
        print("\nThe young man goes to the nearest five guys and gets a big burger for dinner.")
