def start_adventure():
    print("You are in a dark forest. You see a path to the left and a path to the right.")
    choice = input("Which path do you choose? (left/right) ").lower()
    if choice == "left":
        print("You find a treasure chest! Congratulations!")
    elif choice == "right":
        print("You encounter a wild beast and have to retreat.")
    else:
        print("Invalid choice. The adventure ends here.")

if __name__ == "__main__":
    start_adventure()
