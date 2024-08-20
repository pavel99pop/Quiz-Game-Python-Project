print('Welcome to the Computer Quiz!')

playing = input('Are you ready to play?\n')

if playing.lower() != 'yes':
    quit()

print('Good luck! :)\n')
score = 0

answer = input('What does CPU stand for?\n')
if answer.lower() == 'central processing unit':
    print('Correct!\n')
    score += 1
else:
    print('Incorrect!\n')

answer = input('What does GPU stand for?\n')
if answer.lower() == 'graphics processing unit':
    print('Correct!\n')
    score += 1
else:
    print('Incorrect!\n')

answer = input('What does RAM stand for?\n')
if answer.lower() == 'random access memory':
    print('Correct!\n')
    score += 1
else:
    print('Incorrect!\n')

answer = input('What does PSU stand for?\n')
if answer.lower() == 'power supply unit':
    print('Correct!\n')
    score += 1
else:
    print('Incorrect!\n')

print('You got ' + str(score) + ' answers correct!')
print('Your score is ' + str(score  / 4 * 100) + '%')