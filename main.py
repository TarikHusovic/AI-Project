first_question = 'First Question'
second_question = 'Second Question'
third_question = 'Third Question'

questions = [first_question, second_question, third_question]

first_question = ["Do you like to be alone?"]

second_question = ["Do you like to go out?",
                   "Do you have friends"]

third_question = ["Do you like partying?",
                  "Are you suicidal?",
                  "Do you like to play video games?",
                  "Would you like to spend more time with them?"]
answers = [0,0,0]

q1 = first_question[0]
print(q1)
answer1 = int(eval(input("1 for True\n0 for False\nYour answer: ")))

answers[0]=answer1

if answer1 == 0:
    q2 = second_question[0]
    print(q2)
    answer2 = int(eval(input("1 for True\n0 for False\nYour answer: ")))
elif answer1 == 1:
    q2 = second_question[1]
    print(q2)
    answer2 = int(eval(input("1 for True\n0 for False\nYour answer: ")))

answers[1]=answer2

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

answers[2]=answer3

if answers[0] == 0 and answers[1] == 0 and answers[2] == 0:
    print("Call your friends and have a small gathering at your house")
elif answers[0] == 0 and answers[1] == 0 and answers[2] == 1:
    print("Call your friends and have a small party")
elif answers[0] == 0 and answers[1] == 1 and answers[2] == 0:
    print("Try getting a hobby")
elif answers[0] == 0 and answers[1] == 1 and answers[2] == 1:
    print("You have an interesting life")
elif answers[0] == 1 and answers[1] == 0 and answers[2] == 0:
    print("You should try forcing yourself to spend time with other people")
elif answers[0] == 1 and answers[1] == 0 and answers[2] == 1:
    print("Please go get some help, dont kill yourself")
elif answers[0] == 1 and answers[1] == 1 and answers[2] == 0:
    print("You enjoy your life, no need to force any friendships")
elif answers[0] == 1 and answers[1] == 1 and answers[2] == 1:
    print("Call your friends and have a small party")