print('Welcome to Quiz on Python')
answer=input('Are you ready to play the Quiz ? (yes/no) : ')
score=0
total_questions=3
if answer.lower()=='yes':
    answer=input('Question 1: Who is the founder of Python ? ')
    a = 'Guido van Rossum'
    if answer.lower()=='a':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
        print('The correct answer is :',a)
    answer=input('Question 2: Is Python is interpreted language ? ')
    b = 'yes'
    if answer.lower()== b:
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
        print('The correct answer is :',b,'Python is interpreted language')
    answer=input('Question 3: Whether Python is dynamically typed language or statically typed language ? ')
    c = 'dynamically typed language'
    if answer.lower()== c:
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
        print('The correct answer is : Python is dynamically typed language')
print()
print()
print('Thankyou for Playing this small quiz game. You attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print()
print('Marks obtained:',mark)
print()
print('BYE!')
