from random import randint

def diceroll(number, sides):
    result = 0
    for x in range(0,number):
        roll = randint(1,sides)
        result = result + roll
    return result

def dicemenu():
    print("How many dice would you like to roll?")
    qloop = 1
    while qloop:
        try:
            quantity = int(input())
            qloop=0
        except ValueError:
            print("That's not a number, please try again.")
        
    print("How many sides are on your dice?")
    sloop = 1
    while sloop:
        try:
            numberofsides = int(input())
            sloop = 0
        except ValueError:
            print("That's not a number, please try again.")

    print("Your result is: ",diceroll(quantity,numberofsides))

def intro():
    print("Welcome to The Test. This is Placeholder text.")

def main():
    repeat = True

    while repeat:
        print("What would you like to do?")
        commandinput = input().lower()
        command = commandinput.split()
        print("DEBUG: ",command)
        #below will cause a crash if there isn't at least one space in the input, since the split command fails
        if command[1] == "/roll":
            dicemenu()
        if command[1] == "/debug":
            print("placeholder debug menu")
        

        print("Would you like to continue? y/n")
        repeat = ("y" or "yes") in input().lower()

intro()
main()
