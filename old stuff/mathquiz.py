from random import randint
right = 0
lq= 'How many questions would you like to do? '
l= int(input(lq))
for x in range(l):
    num1 = randint(1, 12)
    num2 = randint(1, 12)
    correct = num1 * num2
    question = ' What is ' + str(num1) + ' x ' + str(num2) + '? '
    answer = int(input(question)) 
    if answer == correct:
        print( 'Correct! ')
        right = right + 1
    else:
        print( 'Wrong')   
print("Out of the " + str(l) + " questions. You got " + str(right) + " right" )
if right < l:
    print("Keep studying for a perfect score!")
else:
    print("You got them all correct! Nice!")
