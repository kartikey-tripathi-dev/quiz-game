# To do:
#1.add diff fields and diff difficulty levels
#2.add difficulty wise top scorers

#features
# 1. gets questions from a csv file
# 2. prints name and score in a csv file
# 3. handles the condition when csv question file is not in same folder
# 4. handles if the quiz question file has no questions
# 5. it prints the highest scorers
# 6. it handles user input preventing crashes
# 7. can choose difficulty level
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
        points = 0
        random.shuffle(quiz) #shuffling the quiz  for every round
        name = get_string("Enter Your Name: ").title()

        difficulty = get_diffficulty()

        #using loop to acces individual rows for the questions file
        if difficulty == "All":
            question_count = 0
            for question in quiz:
                ans = get_string(f"{question['Questions']} ({question["Field"]}/{question["Difficulty"]}): ").strip().lower()
                if ans == question['Answers'].lower().strip():
                    points += 1
                    print("Correct!")
                else:
                    print(f"Wrong!, Answer: {question['Answers']}")
                question_count +=1
        else:
            question_count = 0
            for question in quiz:
                if question["Difficulty"] == difficulty:
                    ans = get_string(f"{question['Questions']} ({question["Field"]}/{question["Difficulty"]}): ").strip().lower()
                    if ans == question['Answers'].lower().strip():
                        points += 1
                        print("Correct!")
                    else:
                        print(f"Wrong!, Answer: {question['Answers']}")
                    question_count +=1


        #adding name and points to a dict 
        score =float(f"{100*(points/question_count):.2f}")
        data["Name"] = name
        data["Score"] = score
        data["Difficulty"] = difficulty

        #displaying name and points
        print(f"{name}, you scored: {points}/{question_count}({score})")

       

        #displaying highest scores
        top_scorers  = top_scorers_dict()
        top_score = max(top_scorers.values())   #using max to get int from a list

        if score > top_score:   
            print(f"Congrats You are the highest scorer")

        elif score == top_score:
            print("Congrats You Are among the highest scorers")
            print(name,":",score)
            for i,j in top_scorers.items():
                print(i,":",j)

        else:
            print("Top Scorers")
            for i,j in top_scorers.items():
                print(i,":",j)

        #writing data in csv file
        write_data(data)
        #condition for loop to start again
        play = get_yes_no("Play again? (yes/no)")
#---------------------------------------------------------------------------------------------------------------------------------------------------
def get_questions(file_name):
    try:
            with open(file_name) as file:
                return list(csv.DictReader(file))
    except FileNotFoundError: #checks for quiz_questions.csv file 
        print(f"Please load the file {file_name} to the same folder as quiz.py")
        sys.exit()


 # writing score and name in new file
def write_data(data):
    with open(data_file,"a+",newline = "") as f:
        header = ["Name","Score","Difficulty"]
        writer = csv.DictWriter(f,fieldnames = header)
        f.seek(0)
        if header not in csv.reader(f): 
                writer.writeheader()
        f.seek(0,2)
        writer.writerow(data)

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

def get_diffficulty():
    print("Choose Difficulty")
    print("1.Easy   2.Medium  3.All")
    while True:
        response = get_string("Enter an option (1/2/3): ").lower()
        if response in ("1","one","easy"):
            return "Easy"
        elif response in ("2","two","medium"):
            return "Medium"
        elif response in ("3","three","all"):
            return "All"
        else:
            print("Please enter a valid option")

def top_scorers_dict():
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
                if float(score) > highest_score:
                    highest_score = float(score)
            for content in contents[1:]:
                if not content:
                    continue
                name ,score = content
                if float(score) ==highest_score:
                    d[name] = float(score)
            if d == {}:
                return {0:-1}
            return d
    except FileNotFoundError:
        return {0:-1}        
               
                 
if __name__ == "__main__":
     main()