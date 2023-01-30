print("Think of a number between 1 and 100.")

low = 1
high = 100

while True:
    # computer makes a guess
    guess = (low + high) // 2
    print("Is your number", guess, "?")

    # get user's feedback
    feedback = input("Enter '+' if I should guess higher, '-' if I should guess lower, or 'c' if correct: ")

    if feedback == 'c':
        print("I guessed the correct number! Yay!")
        break
    elif feedback == '-':
        high = guess
    elif feedback == '+':
        low = guess + 1
    else:
        print("Invalid input. Please enter '+', '-', or 'c'.")