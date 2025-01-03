import random

# Step 1: Represent the deck of cards
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

# Step 2: Define functions to operate on the deck

def shuffle_deck(deck):
    """Shuffles the deck of cards."""
    random.shuffle(deck)
    print("\nThe deck has been shuffled!")

def draw_card(deck):
    """Draws a card from the top of the deck."""
    if len(deck) > 0:
        card = deck.pop(0)
        print(f"\nYou drew: {card}")
    else:
        print("\nThe deck is empty!")

def reset_deck():
    """Resets the deck to its full state."""
    return [f"{rank} of {suit}" for suit in suits for rank in ranks]

def display_deck(deck):
    """Displays the current cards in the deck."""
    print("\nCurrent Deck:")
    print(deck)

# Step 3: Main interaction loop
def main():
    print("🎴 Welcome to the Python Deck of Cards Game! 🎴\n")
    print("Menu:")
    print("1. Shuffle the deck")
    print("2. Draw a card")
    print("3. Reset the deck")
    print("4. View the deck")
    print("5. Exit")
    
    current_deck = deck.copy()  # Copy the original deck for operations

    while True:
        choice = input("\nChoose an option (1-5): ")
        if choice == "1":
            shuffle_deck(current_deck)
        elif choice == "2":
            draw_card(current_deck)
        elif choice == "3":
            current_deck = reset_deck()
            print("\nThe deck has been reset!")
        elif choice == "4":
            display_deck(current_deck)
        elif choice == "5":
            print("\nThank you for playing! Goodbye!")
            break
        else:
            print("\nInvalid choice. Please choose between 1-5.")

# Step 4: Run the program
if __name__ == "__main__":
    main()
