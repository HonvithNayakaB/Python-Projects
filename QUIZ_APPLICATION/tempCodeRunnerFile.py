    while True:
            questions=random.shuffel(questions)
            for i in range (10):
                for items in questions[i] [0:5]:
                    print(items)
                    answer=input("please enter your answer = ").lower()
                    if(answer==questions[i][5]):
                        print("Correct answer")
                        score+=1
                    else:
                        print("Incorrect answer\ncorrect answer is = ",questions[i][5])
            print("your total score is =",score)