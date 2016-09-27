#Write a function that prompts the user for input, asking them "Do you want to play again (Y on N)?". If the user answers "Y", the function should return True, otherwise, it should return False.

def play_again():
    answer = raw_input("Do you want to play again (Y or N)? ").lower()
    if answer == "y":
        return True
    else:
        return False
play_again()
