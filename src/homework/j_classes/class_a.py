import random

class Die:

    def roll(self):
        __roll_value = random.randint(1, 6)
        return __roll_value

    def get_roll(self):
        return self.roll()
    
    def __str__(self):
        return str("\nThe rolled value is {0}.\n".format(self.get_roll()))

def main():
    die = Die()
    decision = input("\nWould you like to roll the Die? Y or N.\n\nEnter answer here: ")
    while decision == 'Y':
        print(die)
        decision = input("Would you like to roll the Die again? Y or N.\n\nEnter answer here: ")
    while decision == 'N':
        print("\nYou're no fun, come back later.\n")
        quit()
    else:
        print('\nInvalid input. Enter Y or N.\n')
        main()

main()