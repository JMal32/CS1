import random

def main():
    ans = welcome()
    blnWon = False
    if ans == True:
        print("Lets get started.")
        mypat = genCode()
        for i in range(1,11):
            guess = getPat()
            blnWon = scorePat(guess, mypat)
           # ifblWon: break
        
        if blnWon:
            print("You won! My pattern was:", mypat)
        else:
            print("You lost. It was inevitable, really...")

# Done as of 12 Nov
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

		
def scorePat(code, guess):
    '''generates a score for the given guess (List), as compared to the code (List)
    b = correct color, correct positionindenta
    w = correct color, incorrect position
    prints "Your score is: " + a string of b’s and w’s, or the string "<None>"
    PARAMETERS: guess: the user’s 4-integer guess (List)
​   code: the computer’s secret code (List)
    RETURNS: True or False, to indicate if the game should end (i.e. score==’bbbb’ ==> True)'''
    b = 0
    w = 0
    codes = [] #list for any code integers that did not match the guess in the correct position
    guesses = [] #list for any guess integers that did not match the code in the correct position
    for c, g in zip(code, guess):
        if c == g:
            b += 1
        else:
            codes.append(c)
            guesses.append(g)
    for num in guesses:
        if num in codes:
            w += 1
            codes.remove(num)
    return b, w


    
		
# Done as of 12 Nov
def genCode():
    code = tuple(random.randint(1,6) for i in range(4)) #Used a simple for loop nested in the randint command to get all 4 digits and store them at once
    return code

   
   

# Welcome function is done on Sun Nov 10
def welcome():
    # Welcome message
    print("Welcome to the Python version of Mastermind. To play, I will pick four integers in a random order, then ask you to guess what they are.To win, you must not only guess my four integers, but you must also have them in the correct order. You will have up to 10 guesses. (Note: I can pick the smae integer multiple times).")
    # Prompt the user for "y" or "n"
    while True:
        response = input("Would you like to play a game? Enter 'y'to play, or 'n' to cancel. ").lower()
        if response == "y":
            return True
        elif response == "n":
    	    print("Fine. I didn't want to play with you anyway. Exiting Program...")
    	    return False

        else:
            print("Error: Please enter 'y' or 'n'.")


main()
