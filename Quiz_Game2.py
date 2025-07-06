question = (
    "What is Caleb's full name?: ",
    'How many favorite color does he have?: ',
    'What are his dream jobs? ',
    'What is Calebs birth date?: ',
    'How many country is he a citizen in?: '
)

option = (
    ('A. Caleb Adedeji', 'B. Jason Caleb', 'C.Adedeji Caleb oluwatosin', 'D. Adedeji Tosin'),
    ('A. 2', 'B. 1', 'C. 3', 'D.4'),
    ('A. Software Engineering and Graphic designer', 'B. Full stack Developer and Car detailer', 'C. Graphic Designer', 'D. Barber'),
    ('A. December 30', 'B. June 21', 'C. October 30', 'D. June 3'),
    ('A. 2', 'B. 56', 'C. 3', 'D. 1')
)
answers = ('C', 'A', 'B', 'D', 'A')
guesses = []
score = 0
question_num = 0

for questions in question:
    print('--------------------')
    print(questions)
    for options in option[question_num]:
        print(options)

    guess = input('Enter either (A, B, C, D) to answer ').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('CORRECT!!!')

        if score <= 1:
            print(f' {score} Correct Answer')
        elif score >= 2:
            print(f' {score} Correct Answers')

    else:
        print('Incorrect')
        print(f'{answers[question_num]} is the correct answer')

    question_num +=1

print('----------------------')
print('RESULT')
print('----------------------')

print('The answers ', end='')
for ans in answers:
    print(ans, end='')
print()

print('Your guesses ', end='')
for gue in guesses:
    print(gue, end='')
print()
score = int(score/len(question) * 100)
print(f'Your Total Score is: {score}%')