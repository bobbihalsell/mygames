import peopledata
import random

people = peopledata.data

def random_person():
    """chooses a random person"""
    return random.choice(people)

def format_data(person):
    """Format account into printable format: name, description and country"""
    name = person["name"]
    description = person["description"]
    country = person["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(answer, person1, person2):
    if person1['follower_count']>person1['follower_count']:
        return answer == 'A'
    else:
        return answer == 'B'

def higher_lower():
    continue_game = True
    score = 0
    people_used=[]
    personA = random.choice(people)
    people_used.append(personA)
    personB = random.choice(people)
    while personB in people_used:
        personB = random.choice(people)
    people_used.append(personB)
    while continue_game == True:
        print(f"'\nCompare A: {format_data(personA)}.")
        print('\nvs')
        print(f"\nAgainst B: {format_data(personB)}.")
        guess = input("\nWho has more followers? Type 'A' or 'B': ").upper()
        is_correct = check_answer(guess, personA, personB)
        if is_correct == False:
            continue_game = False
            print(f"\nSorry, that's wrong. Final score: {score}")
        else:
            score+=1
            print(f"\nYou're right! Current score: {score}.")
            personA = personB
            personB = random.choice(people)
            while personB in people_used:
                personB = random.choice(people)
            people_used.append(personB)
            

higher_lower()


