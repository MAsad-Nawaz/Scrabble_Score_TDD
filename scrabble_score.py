import time
import random
# Define the score values for each letter
SCORES = {
    "a": 1, "e": 1, "i": 1, "o": 1, "u": 1, "l": 1, "n": 1, "r": 1, "s": 1, "t": 1,
    "d": 2, "g": 2,
    "b": 3, "c": 3, "m": 3, "p": 3,
    "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
    "k": 5,
    "j": 8, "x": 8,
    "q": 10, "z": 10
}

def scrabble_score(word):
    # Calculate score using the letter values
    total_score = sum(SCORES.get(letter.lower(), 0) for letter in word)
    print(f"Debug: Calculating score for '{word}': {total_score}")  # Debugging line
    return total_score

def is_valid_word(word, dictionary):
    return word.lower() in dictionary

def load_dictionary(file_path='dictionary.txt'):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return set(word.strip().lower() for word in file)
    except FileNotFoundError:
        print(f"Dictionary file '{file_path}' not found.")
        return set()

def get_user_input(word_length):
    print(f"Enter a word with exactly {word_length} letters. You have 15 seconds!")
    start_time = time.time()
    user_word = input("Word: ").strip()
    elapsed_time = time.time() - start_time
    return user_word, elapsed_time

def main():
    dictionary = load_dictionary()
    if not dictionary:
        print("Dictionary could not be loaded. Exiting the game.")
        return
    total_score = 0
    rounds = 0

    while True:
        if rounds >= 10:
            print(f"Game over! Your total score is: {total_score}")
            break
        word_length = random.randint(3, 7)  # Random length between 3 and 7
        user_word, elapsed_time = get_user_input(word_length)

        # Check time limit
        if elapsed_time > 15:
            print("Time's up! No score for this round.")
            continue
        # Validate input length
        if len(user_word) != word_length:
            print(f"Invalid word length. The word should be exactly {word_length} letters long.")
            continue

        # Validate alphabetic characters only
        if not user_word.isalpha():
            print("Invalid input. Please enter a word with only alphabetic characters.")
            continue

        # Validate against dictionary
        if not is_valid_word(user_word, dictionary):
            print("The word is not in the dictionary. Please enter a valid word.")
            continue

        # Calculate score
        word_score = scrabble_score(user_word)
        total_score += word_score
        rounds += 1

        print(f"The Scrabble score for '{user_word}' is {word_score}.")
        print(f"Total score: {total_score}")

        # Ask if the user wants to continue
        continue_game = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_game not in ["yes", "y"]:
            print(f"Game over! Your total score is: {total_score}")
            break

if __name__ == "__main__":
    main()
