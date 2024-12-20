import random

def hangman():
    # List of words
    words = ['python', 'programming', 'developer', 'computer', 'language', 'project', 'coding', 'data']
    word = random.choice(words)

    guessed_word = ["_"] * len(word)  # Jitna words utna underscore
    attempts = 6  # Kitna br galat words guess krna allowed han
    guessed_letter = []

    print("Welcome to Hangman!")
    print("Guess the word:")
    print(" ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()   # Letter guess kerain

        # Agar input valid nhi hai
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        # Agar letter already guess kiya ho
        if guess in guessed_letter:
            print("You already guessed that letter!")
            continue

        guessed_letter.append(guess)  # Guess add karna hai list mein

        if guess in word:
            print(f"Good job! {guess} is in the word.")
            # Sahi letter ko update karna
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1  # Wrong guess par attempts kam hoti hain
            print(f"Wrong guess! You have {attempts} attempts left.")

        print(" ".join(guessed_word))   # Progress dekhte hain

    if "_" not in guessed_word:
        print("\nCongrats! You guessed the word:", word)
    else:
        print("\nYou Lost! The word was:", word)

# Run the game
    hangman()
