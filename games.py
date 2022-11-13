
import random
from words import word_list
import string
import blackjack
from art import rps_pic, hangman_pic, treasure_pic
from peoplehl import higher_lower

# guess the number computer chooses
def number_guess_comp():
    print('YOU ARE GUESSING THE COMPUTERS NUMBER')
    bound = int(input('What should my number be between? 1 - ?  '))
    valid_bound = isinstance(bound, int) and bound>1
    while valid_bound==False:
        bound = int(input('''
        \nPLEASE SELECT AN INTEGER GREATER THAN 1
        \rWhat should my number be between? 1 - ?  '''))
        valid_bound = isinstance(bound, int) and bound>1
    num = random.randint(1, bound)
    guess = 0
    guesses = 0
    while guess != num:
        guess = int(input(f'Choose a number between 1 and {bound} '))
        if guess < num:
            print('nope, too low.')
        elif guess > num:
            print('nope, too high.')
        guesses += 1
    print(f'Congrats! you have guessed {num} correctly in {guesses} guesses!')


# guess the number you chooses
def number_guess_you():
    print('THE COMPUTER WILL GUESS YOUR NUMBER. CHOOSE A NUMBER.')
    bound = int(input('What is your number between? 1 - ?  '))
    valid_bound = isinstance(bound, int) and bound>1
    while valid_bound==False:
        bound = int(input('''
        \nPLEASE SELECT AN INTEGER GREATER THAN 1
        \rWhat is your number between? 1 - ?  '''))
        valid_bound = isinstance(bound, int) and bound>1
    low = 1
    high = bound
    feedback = ' '
    guesses = 0
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low
        feedback = input(f'''\n Is {guess} too high (H) too low (L) or correct (C)? ''').lower()
        if feedback == 'h':
            high = guess - 1
            guesses += 1
        elif feedback == 'l':
            low = guess + 1
            guesses += 1
    print(f'Yay, computer guessed your number, {guess}, correctly in {guesses} guesses!')


def rock_paper_scissors():
    user = input("'r' for rock, 'p' for paper, 's' for scissors  ")
    while user not in ['r', 'p', 's']:
        user = input('''
        \n Please select a valid letter.
        \r 'r' for rock, 'p' for paper, 's' for scissors  ''')
    comp = random.choice(['r', 'p', 's'])
    if comp == 'r':
        print(rps_pic[0])
    elif comp == 'p':
        print(rps_pic[1])
    else:
        print(rps_pic[2])
    if (user == 'r' and comp == 's') or (user == 'p' and comp == 'r') or (user == 's' and comp == 'p'):
        print('You won!')
        return 1
    elif (user == 'r' and comp == 'p') or (user == 'p' and comp == 's') or (user == 's' and comp == 'r'):
        print('You lost')
        return -1
    else:
        print('tie')
        return 0

def rps_best_of(x):
    print(f'YOU ARE PLAYING ROCK PAPER SCISSORS. BEST OF {x}')
    win = 0
    round = 1
    while round <= x:
        win += rock_paper_scissors()
        round += 1
    while win == 0:
        print('''\nITS A TIE!
                 \r play until someone wins''' )
        win += rock_paper_scissors()
    if win > 0:
        print('YOU WIN')
    elif win < 0:
        print('YOU LOSE')



def hangman():
    print('YOU ARE PLAYING HANGMAN')
    word = random.choice(word_list).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed = set()
    tries = 6
    while len(word_letters)>0:
        letter_list = [l if l in guessed else '-' for l in word]
        print(hangman_pic[6-tries])
        print(' '.join(letter_list))
        print('Letters used: ', ' '.join(guessed))
        l = input(f'You have {tries} tries remaining. Guess a letter: ').upper()
        if l in alphabet - guessed:
            guessed.add(l)
            if l in word_letters:
                word_letters.remove(l)
            else:
                tries -=1
        elif l in guessed:
            print(f'You have already guessed {l}. Try again.')
        elif l not in alphabet:
            print(f'please use a valid letter.')
        if tries == 0:
            print(f'Oh no, you ran out of tries, The word was {word}')
            break
    if len(word_letters)==0: 
        print(f'''\n***************************************
                \rCongrats! You guessed {word} correctly!
                \r***************************************''')


# tic tac toe


        



# Band name generator
def band_name():
    place = input("your favourite city you lived in?  ")
    animal = input("what pet do you have/ want?  ")
    print(f'Your band name is {place}s {animal}s!')


def love_calculator():
    print('WelcomE to the loOovEee CAalcuUlatOooOR')
    name1 = input('What is YOUR name?  ').lower()
    name2 = input ('What is THEIR name? ').lower()
    letters = name1 + name2
    true_points = 0
    for i in "true":
        true_points+=letters.count(i)
    love_points = 0
    for i in "love":
        love_points+=letters.count(i)
    points = int(str(true_points) + str(love_points))
    if points < 10 or points >90:
        print(f"Your score is {points}, you go together like coke and mentos.")
    elif points > 40 and points < 50:
        print(f"Your score is {points}, you are alright together." )
    else:
        print(f"Your score is {points}.")



def treasure_island():
    print(treasure_pic)
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    dead = False
    d1 = input("Which direction? Left (L) or Right (R)? ").upper()
    while d1 not in ["L", "R"]:
        d1 = input("Please choose a valid direction. Left (L) or Right (R)? ").upper()
    if d1 == "R":
        dead = True
        print("You have walked into a bears cave. Death by being eaten. GAME OVER")
    elif d1 == "L":
        d2 = input("You have arrived at the lake. What should you do next? Swim (S) or Walk (W)? ").upper()
        while d2 not in ["S", "W"]:
            d2 = input("Please choose a valid decision. Swim (S) or Walk (W)? ").upper()
        if d2 == "S":
            dead = True
            print("Oh no! Death by hypothermia. GAME OVER")
        elif d2 == "W":
            d3 = input("You have found 3 doors, a red door, a yellow door and a blue door./rChoose the one that might have the treasure (R), (Y), (B) ").upper() 
            while d3 not in ['R', 'B', 'Y']:
                d3 = input("Please select a valid door. (R), (Y), (B)")
            if d3 == "B":
                dead = True
                print("You found the room of blues :(. Death by sadness. GAME OVER")
            elif d3 == "Y":
                dead = True
                print("You found the room of lemons. Death by acidity. GAME OVER")
    if dead == False:
        print('CONGRATS YOU HAVE FOUND THE GOLD!')

def encrypt(message, shift):
    alphabet_string = string.ascii_lowercase
    alphabet = list(alphabet_string)
    enc_mess = ""
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index= (index + shift) % 26
            enc_mess += alphabet[new_index]
        else:
            enc_mess += letter
    return enc_mess

def decrypt(message, shift):
    alphabet_string = string.ascii_lowercase
    alphabet = list(alphabet_string)
    dec_mess = ""
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index= (index - shift) % 26
            if new_index < 0:
                new_index+= 26
            dec_mess += alphabet[new_index]
        else:
            dec_mess += letter
    return dec_mess


def ceasar_c():
    again =0
    while again !='N':
        choice = input('Type (E) to encrypt your message and (D) to decrypt your message ').upper()
        while choice not in ['E', 'D']:
            choice = input('Please select a valid option, (E), (D).').upper()
        message = input('Type your message:\n').lower()
        shift = int(input('Type the shift number\n'))
        if choice == 'E':    
            enc = encrypt(message, shift)
            print(f'Your encrypted message is:\n{enc}')
        if choice == 'D':
            dec = decrypt(message, shift)
            print(f'Your decrypted message is:\n{dec}')
        again = input('Would you like to encrypt or decrypt again (Y/N)?\n').upper()
        while again not in ['Y', 'N']:
            again = input('Please select Y or N?\n').upper()






        







# number_guess_comp()
# number_guess_you()
# rock_paper_scissors()
# rps_best_of(3)
# hangman()
# band_name()
# love_calculator()
# treasure_island()
# ceasar_c()



def menu():
    game_choice = '0'
    menu_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'B']
    while game_choice not in menu_choices:
        game_choice = input('''
                        PLEASE SELECT A NUMBER TO PLAY A GAME
                        1) Number Guessing Game - YOU GUESS
                        2) Number Guessing Game - YOU CHOOSE
                        3) Rock Paper Scissors
                        4) Hangman
                        5) Random Band Name Generator
                        6) Love Calculator
                        7) Find the Treasure
                        8) Ceasar Cipher
                        9) Black Jack
                        10) Higher or Lower - celebrities follower count
                        B) BACK
        
                            ''').upper()
    return game_choice


def get_to_game(choice):
    if choice != 'B': 
        if choice == '1':
            number_guess_you()
        elif choice == '2':
            number_guess_comp()
        
        elif choice == '3':
            rounds = int(input('How many rounds would you like to play?  '))
            rps_best_of(rounds)

        elif choice == '4':
            hangman()

        elif choice == '5':
            band_name()
        
        elif choice == '6':
            love_calculator()
        
        elif choice == '7':
            treasure_island()
        
        elif choice == '8':
            ceasar_c()
        
        elif choice == '9':
            blackjack.black_jack()
            
        elif choice == '10':
            higher_lower()

        again = input("To play again type '1' otherwise select any button to return to the main menu")
        if again == '1':
            get_to_game(choice)
    else: 
        menu()







def app():
    name = input('What is your name?  ')
    choice = 1
    while choice != 'E':
        choice = input(f'Hello {name}, would you like to see the game menu (M) or select a game randomly (R) or exit (E)?  ').upper()
        while choice not in ['M', 'R', 'E']:
            choice = input("Please select 'M' for menu or 'R' for a randomly selected game or 'E' to exit ").upper()
        if choice == 'M':
            game_choice = menu()
            get_to_game(game_choice)
        elif choice == 'R':
            random_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', 'B'])
            get_to_game(random_choice)

    print('GOODBYE')

if __name__ == "__main__":
    app()
