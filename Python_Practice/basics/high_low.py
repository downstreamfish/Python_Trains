number = 7
guess = -1
print("guess the number!")
while guess != number:
    guess = int(input("Is it ..."))
    if guess == number:
        print("Hooray! You guessed it right!")
    elif guess < number:
        print("It's bigger...")
    elif guess > number:
        print("It's not so big.")
