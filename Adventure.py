import time

# Define the player's inventory
inventory = []

# Function to display story and prompt for choices
def display_story(story_text, choices):
    print(story_text)
    time.sleep(1)  # Adding delay for better readability
    for idx, choice in enumerate(choices, start=1):
        print(f"{idx}. {choice}")
    while True:
        choice = input("Enter your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(choices):
            return int(choice) - 1
        else:
            print("Invalid choice. Enter a valid option.")

# Function to handle different story paths based on choices
def play_game():
    print("Welcome to the Adventure Game!\n")
    time.sleep(1)

    # Start of the story
    print("You wake up in a mysterious room...")
    time.sleep(2)

    while True:
        # Display story and prompt for choices
        choice = display_story("What do you do?", ["Explore the room", "Look for a way out"])

        # Story path based on the first choice
        if choice == 0:
            print("\nYou find a key hidden under the bed.")
            inventory.append("Key")
            time.sleep(2)
        else:
            print("\nYou discover a hidden door behind the curtains.")
            time.sleep(2)

        # Display story and prompt for choices
        choice = display_story("What's your next move?", ["Use the key on the door", "Search for another way"])

        # Story path based on the second choice
        if choice == 0 and "Key" in inventory:
            print("\nCongratulations! You unlocked the door and escaped!")
            time.sleep(2)
            print("You successfully completed the game.")
            break
        elif choice == 0 and "Key" not in inventory:
            print("\nThe door is locked. You need to find a key.")
            time.sleep(2)
        else:
            print("\nYou keep searching, but there seems to be no other way out.")
            time.sleep(2)
            print("You're trapped and couldn't escape.")
            time.sleep(2)
            print("Game Over.")
            break

# Start the game
play_game()
