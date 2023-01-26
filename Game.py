def start_game():
    print("Welcome to the Adventure!")
    name = input("What is your name? ")
    print("Hello, " + name + "! You find yourself in a dark forest. Do you want to go left or right?")
    choice = input("Enter L for left or R for right: ")
    if choice == "L":
        print("You choose to go left and find a clearing with a small stream.")
        print("Do you want to follow the stream or go back?")
        choice = input("Enter F to follow the stream or B to go back: ")
        if choice == "F":
            print("You follow the stream and find a waterfall. You can't go any further.")
            end_game()
        elif choice == "B":
            print("You go back and find yourself at the fork in the path.")
            start_game()
    elif choice == "R":
        print("You choose to go right and find a cave.")
        print("Do you want to enter the cave or go back?")
        choice = input("Enter E to enter the cave or B to go back: ")
        if choice == "E":
            print("You enter the cave and find a treasure chest!")
            end_game()
        elif choice == "B":
            print("You go back and find yourself at the fork in the path.")
            start_game()

def end_game():
    print("Thanks for playing!")

start_game()
