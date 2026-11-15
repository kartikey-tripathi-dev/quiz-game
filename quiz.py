# To do:
#1. To handle user input (spaces, just enter i.e., "" input)

#features
# 1.gets questions from a csv file
# 2.prints name and score in a csv file
# 3. handles the condition when csv question file is not in same folder
# 3. handles if the quiz question file has no questions

import random
import csv
import sys
#quiz = {"What is the capital of france?": "paris","What is 5 + 7?":"12","Which Planet is the Red Planet?":"mars","How many days in a week?":"7","Which is  the largest ocean?":"pacific","What is 2^10?":"1024"}


try:
    with open("quiz_questions.csv") as file:
        quiz = list(csv.DictReader(file))
except FileNotFoundError: #checks for quiz_questions.csv file 
     print("Please load the file quiz_questions.csv to the same folder as quiz.py")
     sys.exit()

# if file has no quiz questions
if len(quiz) == 0:
     sys.exit("No Quiz Questions to ask")


play = "y"
rows = []
while play == 'y' or play == "yes":
    data = {}
    score = 0
    random.shuffle(quiz) #shuffling the quiz  for every round

    name = input("Enter Your Name: ")

    #using loop to acces individual rows for the questions file
    for i in quiz:
        ans = input(f"{i['Questions']}: ").strip().lower()
        if ans == i['Answers'].lower().strip():
            score += 1
            print("Correct!")
        else:
             print(f"Wrong!, Answer: {i['Answers']}")

    #adding name and score to a dict 
    data["Name"] = name
    data["Score"] = score
    rows.append(data)

    #displaying name and score
    print(f"{name}, you scored: {score}/{len(quiz)}({100*(score/len(quiz)):.2f})")

    #condition for loop to start again
    play = input("Play again?: ").lower()


# writing score and name in new file
with open("Quiz_Data.csv","a+",newline = "") as f:
    header = ["Name","Score"]
    writer = csv.DictWriter(f,fieldnames = header)
    f.seek(0)
    if header not in csv.reader(f):
            writer.writeheader()
    f.seek(0,2)
    writer.writerows(rows)
