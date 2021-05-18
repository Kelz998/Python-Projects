"""
The user needs to answer 3 math questions correctly in a row. 
Desciption says I should use a constant... so I should put my constant
as 3 to represent the number of times correct.
"""

import random
MAX = 100
CORRECT_AMOUNT = 3 #The amount of corrsnt answer user needs in a row.

def main():
    correct_times = 0
    #run in a while loop until 3 correct answers are finished.
    #I want to match the correct amount of times with the amount needed in a row.
    while correct_times != CORRECT_AMOUNT: #while the correct times (0 as of now) is not the same as the constant CORRECT_AMOUNT...
        num1 = random.randint(1, MAX)
        num2 = random.randint(1, MAX)
        print('What is', str(num1), '+', str(num2) + '?')
        answer = int(input('Your answer: '))
        total = num1 + num2 #I need to add the two generated nums, to get the total of the two.
        if answer == total: # If the answer input is the same as the total to the two numbers, it will type correct. Or else, it will reveal the sum.
            correct_times = correct_times + 1 #this seems to work, but it 
            #does not consider answering 3 correct answers in a row. 
            #how can I fix this?
            print("Correct! You've gotten", str(correct_times), 'correct in a row.')
        else:
            print('Incorrect. The answer should be', str(total))
            correct_times = 0
    print('Congratulations! You mastered addition.')

if __name__ == '__main__':
    main()
