import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
computer=random.randint(1,101)
choose=input("Choose a difficulty. Type 'easy' or 'hard': ")

if choose=='easy':
            i=10
            print(f"you have {i} attempt remaining to guess the number.")
            user_guess = int(input(f"Make a guess: "))
            while(i!=0):

                if  user_guess>computer:
                  print(f"you have {i} attempt remaining to guess the number.")
                  print("Too high")
                  user_guess = int(input(f"Make a guess: "))
                if  user_guess<computer:
                    print(f"you have {i} attempt remaining to guess the number.")
                    print("Too low")
                    user_guess = int(input(f"Make a guess: "))
                if user_guess==computer:
                    print(f"got it! the answer was {computer}")
                    exit()
                i=i-1
else:
    i = 6
    print(f"you have {i} attempt remaining to guess the number.")
    user_guess = int(input(f"Make a guess: "))
    while (i != 0):

        if user_guess > computer:
            print(f"you have {i} attempt remaining to guess the number.")
            print("Too high")
            user_guess = int(input(f"Make a guess: "))
        if user_guess < computer:
            print(f"you have {i} attempt remaining to guess the number.")
            print("Too low")
            user_guess = int(input(f"Make a guess: "))
        if user_guess == computer:
            print(f"got it! the answer was {computer}")
            exit()
        i = i - 1

