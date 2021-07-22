"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """
    guard = 0
    while guard < 1000:
        guard += 1
        try:
            user_number = int(input(f"input a number between {low} and {high}: "))
            if low <= user_number <= high:
               return user_number
        except Exception as e:
            print("we couldn't convert that to a number, can you try again please.\n", e)

def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nWelcome to the guessing game!")
    print("A number between 0 and _ ?")
    upperBound = input("Enter an upper bound: ")
    print("OK then, a number between 0 and {} ?".format(upperBound))
    upperBound = int(upperBound)

    actualNumber = random.randint(0, upperBound)

    guessed = False

    while not guessed:
      guessedNumber = int(input("Guess a number: "))
      print("You guessed {},".format(guessedNumber),)
      if guessedNumber == actualNumber:
        print("You got it!! It was {}".format(actualNumber))
        guessed = True
      elif guessedNumber < actualNumber:
        print("Too small, try again :'(")
      else:
        print("Too big, try again :'(")
      return "You got it!"


    low = super_asker(-1000000, 100000, "enter a lower bound")
    high = super_asker(low, 100000, "enter a upper bound")

    actual = random.randint(low, high)

    guard = 0
    while guard < 1000:
          guard += 1
    guess = super_asker(low, high, "Guess a number in this range")
    if guess == actual:
       return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!
    elif guess < actual:
      print("too low, guess higher")
    elif guess > actual:
      print("too high, guess lower")

if __name__ == "__main__":
    print(advancedGuessingGame())
