# To do:
#1.add diff fields and diff difficulty levels

#features
# 1. gets questions from a csv file
# 2. prints name and score in a csv file
# 3. handles the condition when csv question file is not in same folder
# 4. handles if the quiz question file has no questions
# 5. it prints the highest scorers
# 6. it handles user input preventing crashes
import csv
import sys
data_file = "Quiz_Data.csv"
question_file = "quiz_questions.csv"
def main():
    import random
    #quiz = {"What is the capital of france?": "paris","What is 5 + 7?":"12","Which Planet is the Red Planet?":"mars","How many days in a week?":"7","Which is  the largest ocean?":"pacific","What is 2^10?":"1024"}
    quiz = get_questions(question_file)

    # if file has no quiz questions
    if len(quiz) == 0:
        sys.exit("No Quiz Questions to ask")


    play = True
    while play:
        data = {}
        score = 0
        random.shuffle(quiz) #shuffling the quiz  for every round

        name = get_string("Enter Your Name: ").title()

        #using loop to acces individual rows for the questions file
        for i in quiz:
            ans = get_string(f"{i['Questions']}: ").lower()
            if ans == i['Answers'].lower().strip():
                score += 1
                print("Correct!")
            else:
                print(f"Wrong!, Answer: {i['Answers']}")
        

        #adding name and score to a dict 
        data["Name"] = name
        data["Score"] = score
        

        #displaying name and score
        print(f"{name}, you scored: {score}/{len(quiz)}({100*(score/len(quiz)):.2f})")
        #displaying highest scores
        top  = top_scorers()
        if score > max(top.values()):
            print(f"Congrats You are the highest scorer")

        elif score == max(top.values()):
            print("Congrats You Are among the highest scorers")
            print(name,":",score)
            for i,j in top.items():
                print(i,":",j)

        else:
            print("Top Scorers")
            for i,j in top.items():
                print(i,":",j)


        write_data(data)
        #condition for loop to start again
        play = get_yes_no("Play again? (yes/no)")


    # writing score and name in new file
def write_data(data):
    with open(data_file,"a+",newline = "") as f:
        header = ["Name","Score"]
        writer = csv.DictWriter(f,fieldnames = header)
        f.seek(0)
        if header not in csv.reader(f): 
                writer.writeheader()
        f.seek(0,2)
        writer.writerow(data)

def get_questions(file_name):
    try:
            with open(file_name) as file:
                return list(csv.DictReader(file))
    except FileNotFoundError: #checks for quiz_questions.csv file 
        print(f"Please load the file {file_name} to the same folder as quiz.py")
        sys.exit()


def get_string(prompt):
     while True:
            string = input(prompt).strip()
            if string:
                 return string

def get_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y","yes"):
            return True
        elif ans in ("n","no"):
            return False


def top_scorers():
    try:
        with open(data_file) as file:
            contents = list(csv.reader(file))
            if not contents[1:]:
                return {0:-1}
            highest_score = 0
            d = {}
            for content in contents[1:]:
                if not content:
                    continue
                name,score = content
                if int(score) > highest_score:
                    highest_score = int(score)
            for content in contents[1:]:
                if not content:
                    continue
                name ,score = content
                if int(score) == highest_score:
                    d[name] = int(score)
            if d == {}:
                return {0:-1}
            return d
    except FileNotFoundError:
        return {0:-1}        
               
                 
if __name__ == "__main__":
     main()
            
   
                