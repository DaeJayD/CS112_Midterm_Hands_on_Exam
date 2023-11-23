import random

def problem():
    n1 = random.randint(1, 99)
    n2 = random.randint(1, 99)

    operation = random.choice(['+', '-', '*', '/'])

    if operation == '+':
        question = " " + str(n1) + " + " + str(n2) + "?"
        answer = n1 + n2
    elif operation == '-':
        question = " " + str(n1) + " - " + str(n2) + "?"
        answer = n1 - n2
    elif operation == '*':
        question = " " + str(n1) + " x " + str(n2) + "?"
        answer = n1 * n2
    else:
        n1, n2 = max(n1, n2), min(n1, n2)
        question = " " + str(n1) + " / " + str(n2) + "?"
        answer = n1 // n2

    return question, answer

while True:

    question, answer = problem()

    print(question)

    student_answer = int(input("Your answer: "))

    if student_answer == answer:
        print("Correct! " + str(question) + " = " + str(answer) + "\n")
    else:
        print("Wrong! The correct answer is " + str(answer) + "\n")
