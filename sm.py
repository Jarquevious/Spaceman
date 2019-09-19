import random 
import string
def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r') #open the file and 'r' keeps it open
    words_list = f.readlines() #read line means everything is in the open file, all words are being added to the word list
    f.close() #means it closed

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for letter in secret_word:
        if letter in letters_guessed:
            continue
        else:
            return False
    
    return True
    
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    answer = ""
    for letter in secret_word:
        if letter in letters_guessed:
            answer += letter
        else:
            answer += "_"
    return answer 

  
def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    if guess in secret_word:
        return True
    elif guess in secret_word:
        return False 
    else:
        print("something is")
    #TODO: check if the letter guess is in the secret word


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    #TODO: show the player information about the game according to the project spec
    print(f"Welcome to Spaceman\nThe Secret word contains: {len(secret_word)} letters")
    print(secret_word)
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    letters_guessed = list()
    
    Counter = 7
    while Counter > 0:
        print("---------------------------------------------------")
        guess = str(input("Guess a letter: "))
        
        #A while loop to check length of user input. similiar to guess in letters_guessed
        while len(guess) != 1:
            guess = str(input("Sorry, you can only use one letter at a time, please try again!: "))

        #Another while loop to check if it is a letter
        while str.isalpha(guess) == False:
            guess = str(input("Sorry, you can only use a letter, please try again!: "))

        while guess in letters_guessed:
            guess = str(input("You entered that letter already, try again: "))
        
        letters_guessed.append(guess)
        
        print(get_guessed_word(secret_word, letters_guessed))

        if is_guess_in_word(guess, secret_word) == True:
            print("Correct!")
        else:
            print("Incorrect!")
            Counter -= 1
        print(f"Letters guessed {letters_guessed}")
        
        alpha.remove(guess)
        
        print(f"You have {Counter} guesses left")
        print("Letters you have left: ", " ".join(alpha))
        
        
        if is_word_guessed(secret_word, letters_guessed) == True:
            return print("Congrats!  You have won the game!")

        if Counter < 1: 
            print("GAME OVER! YOU LOOSE!!! LOSER!!!")
   
    #if Counter == 0:
        
    #else:
        #print( "Congrats!  You have won the game!")


    


    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
   
    #TODO: show the guessed word so far
    #TODO: check if the game has been won or lost
    






#These function calls that will start the game
secret_word = load_word()
#spaceman(secret_word)

def test_function():
    print(load_word())
    print(is_word_guessed(secret_word, "a"))
    print(is_guess_in_word("a", secret_word))

test_function()