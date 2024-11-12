import random

def main():
    ans = welcome()
    blnWon = False
    if ans:
        print("Let's get started.")
        mypat = genCode()
        for i in range(1, 11):
            guess = getPat()
            b, w = scorePat(guess, mypat)
            print(f"Your current score is: {b} b's and {w} w's")
        
        if blnWon:
            print("You won! My pattern was:", mypat)
        else:
            print("You lost. It was inevitable, really...")

# Function to get the player's guess
def getPat():
    while True:
        try:
            player_num = input("Enter your guess as four numbers between 1 and 6 (no spaces): ")
            
            # Check if the input is exactly four digits long and consists only of digits
            if len(player_num) != 4 or not player_num.isdigit():
                print("Error: You must enter exactly four digits.")
                continue  # Ask again if input is invalid

            # Convert each character to an integer and validate the range
            numbers = [int(num) for num in player_num]
            if all(1 <= num <= 6 for num in numbers):
                print(f"Proceeding with numbers: {numbers}")
                return numbers  # Return the valid numbers to proceed
            else:
                print("Error: Each number must be between 1 and 6.")
        
        except ValueError:
            print("Error: Invalid input. Please enter four digits.")

# Function to compare the guess with the code and provide feedback
def scorePat(guess, code):
    '''Generates a score for the given guess (List), as compared to the code (List)
    b = correct integer and position, w = correct integer but incorrect position
    Returns True if the guess matches the code exactly (4 'b's), otherwise False'''
    b = 0  # Correct integer and position
    w = 0  # Correct integer but wrong position
    
    # Track non-matching elements
    codes= []
    guesses = []
    
    for c, g in zip(code, guess):
        if c == g:
            b += 1
        else:
            codes.append(c)
            guesses.append(g)
    
    for num in guesses:
        if num in codes:
            w += 1
            codes.remove(num)  # Remove to prevent double-counting
    
    # Print the score for feedback
    print(f"Score: {b} 'b' and {w} 'w'")
    
    # Return True if the player has won (4 correct positions), otherwise False
    return b == 4

# Function to generate a random 4-digit code
def genCode():
    code = [random.randint(1, 6) for i in range(4)]
    return code

# Welcome function to start the game
def welcome():
    print("Welcome to the Python version of Mastermind. To play, I will pick four integers in a random order, then ask you to guess what they are.")
    print("To win, you must not only guess my four integers, but you must also have them in the correct order.")
    print("You will have up to 10 guesses. (Note: I can pick the same integer multiple times).")
    
    while True:
        response = input("Would you like to play a game? Enter 'y' to play, or 'n' to cancel: ").lower()
        if response == "y":
            return True
        elif response == "n":
            print("Fine. I didn't want to play with you anyway. Exiting Program...")
            return False
        else:
            print("Error: Please enter 'y' or 'n'.")


if __name__ == __main__:
    main()