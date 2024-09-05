import time
import random
import string

# Define the score values for each letter
scores = {
    "a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2,
    "h": 4, "i": 1, "j": 8, "k": 5, "l": 1, "m": 3, "n": 1,
    "o": 1, "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1,
    "v": 4, "w": 4, "x": 8, "y": 4, "z": 10
}

def scrabble_score(word):
    total = 0
    for letter in word.lower():
        if letter in scores:
            total += scores[letter]
    return total

def is_valid_word(word, dictionary):
    return word.lower() in dictionary

def load_dictionary():
    # Here you should load a real dictionary; for simplicity, use a small set of words
    return {"apple", "banana", "cherry", "date", "grape", "kiwi", "lemon"}

def main():
    dictionary = load_dictionary()
    total_score = 0
    rounds = 0

    while True:
        if rounds >= 10:
            print(f"Game over! Your total score is: {total_score}")
            break
        
        word_length = random.randint(3, 7)  # Random length between 3 and 7
        print(f"Enter a word with exactly {word_length} letters. You have 15 seconds!")

        start_time = time.time()
        user_word = input("Word: ").strip()

        elapsed_time = time.time() - start_time
        if elapsed_time > 15:
            print("Time's up!")
            continue
        
        if len(user_word) != word_length:
            print(f"Invalid word length. The word should be exactly {word_length} letters long.")
            continue
        
        if not user_word.isalpha():
            print("Invalid input. Please enter a word with only alphabetic characters.")
            continue
        
        if not is_valid_word(user_word, dictionary):
            print("The word is not in the dictionary. Please enter a valid word.")
            continue

        word_score = scrabble_score(user_word)
        total_score += word_score
        rounds += 1

        print(f"The scrabble score for '{user_word}' is {word_score}.")
        print(f"Total score: {total_score}")

        continue_game = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_game != "yes":
            print(f"Game over! Your total score is: {total_score}")
            break

if __name__ == "__main__":
    main()
