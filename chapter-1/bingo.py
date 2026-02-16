# imports and global variables 
import random

MAX_NUM = 10
MIN_NUM = 1
max_guess_counts = 3

# generate a random numbers
def generate_random_num():
    return random.randint(MIN_NUM,MAX_NUM)


# get user inputs as guess 
def get_user_inputs():
    print(f"your number should be between {MIN_NUM}-{MAX_NUM}")
    while True :
        try:
            user_inputs = int(input("enter your guess :"))
        except ValueError:
            print("Error: enter a valid number")
        else:
            return user_inputs
        
# check guessed number
def check_guessed_number(user_inputs,random_num):
    return user_inputs == random_num

# main function for running application 
def main():
    global max_guess_counts
    random_num = generate_random_num()
    print(f"random number is : {random_num}")
    while max_guess_counts > 0:
        user_inputs = get_user_inputs()
        if check_guessed_number(user_inputs,random_num):
            print("you have guessed right")
            break
        max_guess_counts -=1
        print(f"guesses left:{max_guess_counts}")
    else:
        print("you couldn't guess the number, and run out of guesses")
        
if __name__ == "__main__":
    main()