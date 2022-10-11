#Asks user for their grade as a number and returns the value as a letter.
#Example: Entering a grade of 78 returns C+.

all_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'] #List stores all letter grades.

def display_grade(num_grade, position): #Returns percent grade and letter grade.
    return (f'With a grade of {num_grade}, you get an {all_grades[position]}.')


def get_letter_grade(num_grade): #Based on user input, calls display_grade with appropriate reference for the list.
    if 97 <= num_grade <= 100:
        return display_grade(num_grade, 0)
    elif 93 <= num_grade < 97:
        return display_grade(num_grade, 1)
    elif 90 <= num_grade < 93:
        return display_grade(num_grade, 2)
    elif 87 <= num_grade < 90:
        return display_grade(num_grade, 3)
    elif 83 <= num_grade < 87:
        return display_grade(num_grade, 4)
    elif 80 <= num_grade < 83:
        return display_grade(num_grade, 5)
    elif 77 <= num_grade < 80:
        return display_grade(num_grade, 6)
    elif 73 <= num_grade < 77:
        return display_grade(num_grade, 7)
    elif 70 <= num_grade < 73:
        return display_grade(num_grade, 8)
    elif 67 <= num_grade < 70:
        return display_grade(num_grade, 9)
    elif 63 <= num_grade < 67:
        return display_grade(num_grade, 10)
    elif 60 <= num_grade < 63:
        return display_grade(num_grade, 11)
    elif 0 <= num_grade < 60:
        return display_grade(num_grade, 12)
    else:
        return ('That is an invalid selection.')

def ask_for_grade(): #Asks user for their grade as a percentage.
    print('What is your grade percentage?')
    grade_percentage = float(input())

    return get_letter_grade(grade_percentage)


print(ask_for_grade())