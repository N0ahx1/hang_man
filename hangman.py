import requests

def get_random_word():
    url = "https://random-word-api.herokuapp.com/word?number=1"
    response = requests.get(url)
    word = response.json()[0]
    return word.upper()

def play_hangman():
    word = get_random_word()
    word_letters = set(word)
    alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    used_letters = set()

    lives = 6
    
    hangman_images = [
    '''
    +---+
    |   |
        |
        |
        |
        |
    ========= 
    ''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    ========= 
    ''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    ========= 
    ''',
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    ========= 
    ''',
    '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    ========= 
    ''',
    '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    ========= 
    ''',
    '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    ========= 
    '''
]

    


    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in word.")
                print(hangman_images[5-lives])
        elif user_letter in used_letters:
            print("You have already used that letter. Guess another letter.")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print("You died, sorry. The word was", word)
        print(hangman_images[6])
    else:
        print("YAY! You guessed the word and survived!", word, "!!")

play_hangman()
