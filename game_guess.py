import random 

def welcome():
    print("Welcome to this funny game")
    print("I will guess a number between 1 100 and")
    print("you have to guess it...")
    print("go go go")
    print()

def finish():
    print("Good game")
    print(f"my number was {number} and you found it in {count}")
    print("")
    answer = input("Do you want to play again ? (Y/N)")
    if answer .upper() == 'Y':
        return True
    else:
        return False

def win(computer_number, guess):
    return computer_number == guess

def answer(computer, user):
    if computer > user:
        return "My number is larger"
    if computer  < user:
        return "ohh.. you went so large! mine is smaller"
    
    return "Wow! you won! Good guess!"

def get_guess():
    ans = input("What is your guess")
    return int(ans)


welcome()
continue_playing = True
while (continue_playing):
    #computer number between 1 to 20 
    computer_number = random.randint(1, 20)
    
    #satrt whit wrong guess
    guess = 0 
    
    count = 0 

while (not win (computer_number, guess)):
    guess = get_a_guess()
    
    count += 1
    print(answer(computer_number, guess))
        
    continue_playing = finish(computer_number, count)
