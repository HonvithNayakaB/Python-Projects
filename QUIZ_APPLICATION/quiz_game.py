import random
questions=[
        ["Who is known as the 'Father of Computers'?" , "a) Charles Babbage" , " b) Alan Turing" , " c) Bill Gates" , " d) Steve Jobs", "a"],
        ["Which planet is known as the 'Red Planet'?" , " a) Venus" , " b) Earth" , " c) Mars" , " d) Jupiter", "c"],
        ["What is the capital city of Japan?" , " a) Beijing" , " b) Seoul" , " c) Tokyo" , " d) Bangkok", "c"],
        ["Which element has the chemical symbol 'O'?" , " a) Gold" , " b) Oxygen" , " c) Osmium" , " d) Ozone", "b"],
        ["Which ocean is the largest in the world?" , " a) Atlantic Ocean" , " b) Indian Ocean" , " c) Arctic Ocean" , " d) Pacific Ocean", "d"],
        ["Who painted the Mona Lisa?" , " a) Vincent van Gogh" , " b) Pablo Picasso " , "c) Leonardo da Vinci" , " d) Claude Monet", "c"],
        ["Which country is known as the Land of the Rising Sun? " , "a) China " , "b) Japan " , "c) Korea " , "d) Thailand", "b"],
        ["Who discovered gravity? " , "a) Albert Einstein " , "b) Isaac Newton " , "c) Galileo Galilei " , "d) Nikola Tesla", "b"],
        ["Which element has the chemical symbol 'H'? " , "a) Hydrogen " , "b) Helium " , "c) Mercury " , "d) Nitrogen", "a"],
        ["In which year did World War II end? " , "a) 1940 " , "b) 1945 " , "c) 1939 " , "d) 1950", "b"],
        ["Which country is the largest by area? " , "a) United States " , "b) China " , "c) Russia " , "d) Canada", "c"],
        ["What is the longest river in the world? " , "a) Amazon River " , "b) Nile River " , "c) Mississippi River " , "d) Yangtze River", "b"],
        ["Which planet is closest to the Sun? " , "a) Earth " , "b) Mercury " , "c) Venus " , "d) Mars", "b"],
        ["Who invented the telephone? " , "a) Nikola Tesla " , "b) Thomas Edison " , "c) Alexander Graham Bell " , "d) Samuel Morse", "c"],
        ["Which famous scientist developed the theory of relativity?" , " a) Isaac Newton" , " b) Nikola Tesla" , " c) Albert Einstein " , "d) Marie Curie", "c"],
        ["What is the capital of France?" , " a) Rome" , " b) Paris" , " c) Madrid" , " d) Berlin", "b"],
        ["Which country has the largest population in the world? " , "a) India" , " b) United States " , "c) China " , "d) Brazil", "a"],
        ["What is the currency of the United Kingdom?" , " a) Dollar b) " , "Euro " , "c)Pound Sterling d) " , "Franc", "c"],
        ["Who is the author of the Harry Potter series? " , "a) J.R.R. Tolkien " , "b) J.K. Rowling " , "c) Suzanne Collins " , "d) George R.R. Martin", "b"],
        ["Which is the smallest country in the world? " , "a) Monaco b" , ") Vatican City " , "c) San Marino " , "d) Liechtenstein", "b"]
]

score=0
print("welcome to the QUIZ GAME \nplease enter start to start the game\nand exit to exit the game")
while True:
    order=input().lower()
    if(order=="start"):
        random.shuffle(questions)
        for i in range (10):
            for items in questions[i][0:5]:
                print(items)
            answer=input("please enter your answer = ").lower()
            if(answer==questions[i][5]):
                print("Correct answer")
                score+=1
            else:
                print("Incorrect answer\ncorrect answer is = ",questions[i][5])
        print("your total score is =",score)
    elif(order=="exit"):
        print("exiting from the game..")
        break
    else:
        print("please enter start to play the game")


