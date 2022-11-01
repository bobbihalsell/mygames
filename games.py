
import random
from words import word_list
import string

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
    print(f'Congrats! you have guessed {num} correctly in {guess} guesses!')


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
    tries = 10
    while len(word_letters)>0:
        letter_list = [l if l in guessed else '-' for l in word]
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
        




# number_guess_comp()
# number_guess_you()
# rock_paper_scissors()
# rps_best_of(3)
# hangman()


def menu():
    game_choice = '0'
    menu_choices = ['1', '2', '3', '4', 'B']
    while game_choice not in menu_choices:
        game_choice = input('''
                        PLEASE SELECT A NUMBER TO PLAY A GAME
                        1) Number Guessing Game - YOU GUESS
                        2) Number Guessing Game - YOU CHOOSE
                        3) Rock Paper Scissors
                        4) Hangman
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

        again = input("To play again type '1' otherwise select any button to return to the main menu")
        if again == '1':
            get_to_game(choice)
    else: 
        pass







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
            random_choice = random.choice(['1', '2', '3', '4'])
            get_to_game(random_choice)

    print('GOODBYE')

app()
