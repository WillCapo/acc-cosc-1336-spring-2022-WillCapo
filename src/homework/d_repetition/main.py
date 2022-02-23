import repetition

choice = int(input('\nHomework 3 Menu\n\n1-Factorial\n2-Sum odd numbers\n3-Exit\n\nPlease choose an option: '))

if(choice == 1):
    input = int(input('\nEnter a number: '))
    if(input < 0 or input > 10):
        print('\nEnter a number between 0 and 10 next time.')
    print('\nYour factorial is ' + str(repetition.get_factorial(input)) + '\n')

if(choice == 2):
    input = int(input('\nEnter a number: '))
    if(input < 0 or input > 100):
        print('\nEnter a number between 0 and 100 next time.')
    print('\nYour total is ' + str(repetition.sum_odd_numbers(input)) + '\n')

if(choice == 3):
    print('\nExiting menu.\n')