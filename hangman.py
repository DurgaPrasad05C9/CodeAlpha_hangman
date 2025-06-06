import random

word_list = [
    ("python", "A popular programming language with a snake logo."),
    ("sunset", "Beautiful view when the day ends."),
    ("robot", "A machine that can perform tasks automatically."),
    ("laptop", "A portable device used for coding and browsing."),
    ("guitar", "A musical instrument with strings.")
]

secret_word, hint = random.choice(word_list)
guessed_word = ["_"] * len(secret_word)
guessed_letters = []
max_incorrect_guesses = 5
incorrect_guesses = 0

print("🎮 Welcome to Hangman!")
print("🧠 Hint:", hint)
print("🔤 Guess the word: " + " ".join(guessed_word))

while incorrect_guesses < max_incorrect_guesses and "_" in guessed_word:
    guess = input("➡️ Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for idx, letter in enumerate(secret_word):
            if letter == guess:
                guessed_word[idx] = guess
        print("✅ Correct!")
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

    print("📝 Current word: " + " ".join(guessed_word))
    print("🔁 Guessed letters: " + ", ".join(guessed_letters))

if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game over! The word was:", secret_word)
