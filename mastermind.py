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
'''		
 PARAMETERS: NONE
   Elicits four integers from the user in the range [1..6]; Prints onscreen the four integers it has read in (this confirms to the user what the program has read in!)
   Returns: a bulletproof list of four integers provided by the user

def getPat():
	try:
		player_num = int(input("Enter four numbers between 1 and 6: "))
		numbers = [int(num) for num in player_num.split()]
		if len(numbers) != 4:
			print("Error: you must enter exactly four numbers.")
	        # Check if the number is within the range
	    for num in numbers:
			if not (1 <= num <= 6):
				print("Error: Number must be between 1 and 6.")
	    	else:
				print(f"Proceeding with number {numbers}.")
		return numbers
	except ValueError:
		print("Error: You must enter an integer.")
		
def scorePat(guess, code):
    generates a score for the given guess (List), as compared to the code (List)
    b = correct color, correct positionindenta
    w = correct color, incorrect position
    prints "Your score is: " + a string of b’s and w’s, or the string "<None>"
    PARAMETERS: guess: the user’s 4-integer guess (List)
​   code: the computer’s secret code (List)
    RETURNS: True or False, to indicate if the game should end (i.e. score==’bbbb’ ==> True)'''
		

def genCode():
   ''' computer CodeMaker generates a sequence of four random integers from [1..6]
    PARAMETERS: None
    RETURNS: a tuple of four random integers from [1..6]

   
   

# Welcome function is done on Sun Nov 10
def welcome():
    # Welcome message
    print("Welcome to the Python version of Mastermind. To play, I will pick four integers in a random order, then ask you to guess what they are. To win, you must not only guess my four integers, but you must also have them in the correct order. You will have up to 10 guesses. (Note: I can pick the smae integer multiple times).")
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
'''
