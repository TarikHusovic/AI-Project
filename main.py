first_question = 'First Question'
second_question = 'Second Question'
third_question = 'Third Question'

questions = [first_question, second_question, third_question]

first_question = ["Do you like to be alone?"]

second_question = ["1.1",
                   "1.2"]

third_question = ["21",
                  "22 math question",
                  "23 math question",
                  "24 math question"]

result = {"Correct": 0, "Incorrect": 0}


def get_answer(question, correct_answer):
    while True:
        try:
            print("Question: {}")
            answer = int(eval(input("1 for True\n0 for False\nYour answer: ")))
        except ValueError:
            print("Not a number, please try again\n")
        else:
            if answer is not 0 and answer is not 1:
                print("Invalid value, please try again\n")
            elif bool(answer) is correct_answer:
                result["Correct"] += 1
                return True
            else:
                result["Incorrect"] += 1
                return False


q1 = first_question[0]
print(q1)
answer1 = int(eval(input("1 for True\n0 for False\nYour answer: ")))
if answer1 == 1:
    q2 = second_question[0]
    print(q2)
    answer2 = int(eval(input("1 for True\n0 for False\nYour answer: ")))
elif answer1 == 0:
    q2 = second_question[1]
    print(q2)
    answer2 = int(eval(input("1 for True\n0 for False\nYour answer: ")))
if answer2 == 0 and answer1 == 0:
    q3 = third_question[0]
    print(q3)
    answer3 = int(eval(input("1 for True\n0 for False\nYour answer: ")))
elif answer2 == 0 and answer1 == 1:
    q3 = third_question[1]
    print(q3)
    answer3 = int(eval(input("1 for True\n0 for False\nYour answer: ")))
elif answer2 == 1 and answer1 == 0:
    q3 = third_question[2]
    print(q3)
    answer3 = int(eval(input("1 for True\n0 for False\nYour answer: ")))
elif answer2 == 1 and answer1 == 1:
    q3 = third_question[3]
    print(q3)
    answer3 = int(eval(input("1 for True\n0 for False\nYour answer: ")))
