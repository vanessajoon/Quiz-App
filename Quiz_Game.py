#my python quiz game
questions  = (
    'What is Vanessa full name: ',
    'What are her dream jobs?: ',
    'How many favorite colors does she have?: ',
    'Who is her go to person?: ' ,
    'What is her religion?: '
)

options = (
    ('A. Vanessa Bree', 'B. Ifechi Jideonwo ', 'C. Vanessa Ifechi Jideonwo', 'D. Jideonwo Vanessa'),
    ('A. Medicine and Software Engineering', 'B. Cybersecurity and Plastic Surgeon', 'C. Cybersecurity and Software Engineering', 'D. Stylist and Tailor'),
    ('A. 3', 'B. 1', 'C. 2', 'D. 4'),
    ('A. Damilola', 'B. Caleb', 'C. Jessica', 'D. Success'),
    ('A. Muslim', 'B. Atheists', 'C. Traditional Worshipper', 'D. Christian')
)

answers = ('C', 'B', 'A', 'B', 'D')

guesses = []
score = 0
question_num = 0

for question in questions:
    print('------------------------------------')
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input('Enter (A, B, C, D): ').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print('CORRECT!!!')
    else:
        print('INCORRECT!!!')
        print(f'{answers[question_num]} is the correct answer')
    question_num+=1

print('------------------------------------')
print('       RESULTS      ')
print('------------------------------------')

print('answer', end=' ')
for answer in answers:
    print(answer, end=' ')
print()

print('guesses', end=' ')
for g in guesses:
    print(g, end=' ')
print()

score = int(score/len(questions) * 100)
print(f'Your score is: {score}%')