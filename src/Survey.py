
ans = input ("What is your id number: ")

class Question:
     def __init__(self, prompt, answer, choices):
          self.prompt = prompt
          self.answer = answer
          self.choices = choices

question_prompts = [
     "\nWhat is your favorite type of food?\n(1)Asian\n(2)Italian\n(3)American\n(4)British\nAns: ",
     "\nWhere in the world would you want to travel to?\n(1)South Korea\n(2)England\n(3)Japan\n(4)Germany\nAns: ",
     "\nWhat dog would you want?\n(1)Yorkie\n(2)Husky\n(3)Australian Shepherd\n(4)Not a dog owner\nAns: ",
     "\nWhat is your favorite sport to watch?\n(1)Football\n(2)Soccer\n(3)Tennis\n(4)Tae Kwon Do\nAns: ",
     "\nWhat type of music to you like?\n(1)Rock and Roll\n(2)Country\n(3)K-Pop\n(4)Classical\nAns: ",
     ]

questions = [
     Question(question_prompts[0], "1", [1,2,3,4]),
     Question(question_prompts[1], "1", [1,2,3,4]),
     Question(question_prompts[2], "1", [1,2,3,4]),
     Question(question_prompts[3], "1", [1,2,3,4]),
     Question(question_prompts[4], "1", [1,2,3,4]),
     ]

def run_quiz(questions):
     score = 0
     writefile = open ('SurveyAnswers.txt', 'a')
     writefile.write(str(ans))
     writefile.write("\n")
     writefile.close()
     for question in questions:
          answer = input(question.prompt)
          while not int(answer) in question.choices:
               print("Invalid Option! Choose Again!")
               answer = input(question.prompt)
          writefile = open ('SurveyAnswers.txt', 'a')
          writefile.write(str(answer))
          writefile.write("\n")
          writefile.close()
          if answer == question.answer:
               score += 1
     print("\nThank You for Participating!")
     print("You're answers will be sent to your email shortly.")

run_quiz(questions)
