import random

# List of anime characters with their descriptions and hints
anime_characters = [
    {
        "name": "Naruto Uzumaki",
        "description": "A ninja from the Hidden Leaf Village who dreams of becoming the Hokage.",
        "hint": "Loves ramen and has a nine-tailed fox spirit within him."
    },
    {
        "name": "Luffy",
        "description": "A pirate with a straw hat who dreams of becoming the Pirate King.",
        "hint": "Can stretch his body like rubber."
    },
    {
        "name": "Goku",
        "description": "A Saiyan warrior with spiky black hair and a love for fighting strong opponents.",
        "hint": "Can transform into a golden-haired Super Saiyan."
    },
    {
        "name": "Sailor Moon",
        "description": "A schoolgirl who transforms into a magical warrior with a sailor outfit.",
        "hint": "Fights for love and justice with her Moon Stick."
    },
    {
        "name": "Levi Ackerman",
        "description": "An incredibly skilled soldier known for his talent with swords and obsession with cleanliness.",
        "hint": "Part of the Scout Regiment and famous for fighting Titans."
    },
    {
        "name": "Deku",
        "description": "A young hero in training who inherited a powerful quirk.",
        "hint": "His real name is Izuku Midoriya, and his idol is All Might."
    },
]

def display_menu():
    print("\nAnime Character Guessing Game")
    print("1. Start Game")
    print("2. Exit")

def anime_guessing_game():
    # Shuffle the character list
    random.shuffle(anime_characters)
    
    score = 0
    total_rounds = len(anime_characters)
    
    for i, character in enumerate(anime_characters):
        attempts = 3
        print(f"\nRound {i+1}/{total_rounds}")
        print("Description: " + character["description"])
        
        while attempts > 0:
            guess = input("Who is this character? ").strip()
            
            if guess.lower() == character["name"].lower():
                print("Correct! 🎉")
                score += 1
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Incorrect! You have {attempts} attempt(s) left. Here's a hint: {character['hint']}")
                else:
                    print(f"Out of attempts! The correct answer was: {character['name']} 😢")
    
    # Final score
    print("\nGame Over!")
    print(f"Your final score is {score}/{total_rounds}.")
    if score == total_rounds:
        print("Incredible! You are an anime expert! 🌟")
    elif score >= total_rounds // 2:
        print("Nice work! You did well! 😊")
    else:
        print("Better luck next time! Keep watching anime! 🍥")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            anime_guessing_game()
        elif choice == '2':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Run the game
main()
