# Basic Quiz Game in Python

def start_quiz(questions):
    score = 0
    for question, options, correct_answer in questions:
        print(question)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        answer = input("Enter your answer (1/2/3/4): ")
        if answer.isdigit() and int(answer) == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer.")
        print()  # Blank line for readability between questions

    print(f"Quiz completed! Your score is {score}/{len(questions)}.")

# List of questions. Each question is a tuple containing the question text,
# a list of options, and the index of the correct answer (1-based).
questions = [
    ("What is the capital of France?", ["1) London", "2) Paris", "3) Berlin", "4) Madrid"], 2),
    ("What is 2 + 2?", ["1) 3", "2) 4", "3) 5", "4) 6"], 2),
    ("Who wrote Hamlet?", ["1) Tolkien", "2) Shakespeare", "3) Austen", "4) Hemingway"], 2),
    ("Which gas is most abundant in the Earth's atmosphere?", ["1) Oxygen", "2) Hydrogen", "3) Carbon Dioxide", "4) Nitrogen"], 4),
    ("What is the largest planet in our solar system?", ["1) Earth", "2) Mars", "3) Jupiter", "4) Saturn"], 3),
    ("In what year did the Titanic sink?", ["1) 1912", "2) 1905", "3) 1898", "4) 1923"], 1),
    ("Which element has the chemical symbol 'O'?", ["1) Gold", "2) Oxygen", "3) Osmium", "4) Olmium"], 2),
    ("Who is known as the father of computer science?", ["1) Albert Einstein", "2) Isaac Newton", "3) Charles Babbage", "4) Alan Turing"], 3),
    ("What is the hardest natural substance on Earth?", ["1) Diamond", "2) Quartz", "3) Gold", "4) Iron"], 1),
    ("Which country is known as the Land of the Rising Sun?", ["1) China", "2) Australia", "3) Japan", "4) South Korea"], 3),
]


if __name__ == "__main__":
    print("Welcome to the Basic Quiz Game!")
    start_quiz(questions)
