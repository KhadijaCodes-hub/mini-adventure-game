name = input("Enter your name : ")
print(f"Welcome {name} to the Adventure Game!")

print("\nYou wake up in a dark forest. Two paths lie ahead.")
choice1 = input("Do you go LEFT or RIGHT? ").lower()

if choice1 == "left":
    print("\nYou find a calm river.")
    choice2 = input("Do you SWIM across or BUILD a raft? ").lower()

    if choice2 == "swim":
        print("\nThe current is too strong. You drown. 💀 Game Over.")
    elif choice2 == "build":
        print("\nSmart move! You safely cross the river and find treasure! 🏆")
    else:
        print("\nInvalid choice. A wild bear eats you. 🐻")

elif choice1 == "right":
    print("\nYou find a cave.")
    choice2 = input("Do you ENTER the cave or KEEP walking? ").lower()

    if choice2 == "enter":
        print("\nInside, you find gold guarded by a dragon. 🐉 You quietly escape with some coins. You win!")
    elif choice2 == "keep":
        print("\nYou get lost in the forest and never return. 🌲 Game Over.")
    else:
        print("\nYou hesitate too long... and night falls. You’re never seen again. 🌑")

else:
    print("\nYou stand still until you vanish into the mist. 👻")
