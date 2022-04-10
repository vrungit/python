
from data import question_data
from question_model import Question
import os


question_bank = []

for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["text"],question_data[i]["answer"]))

print(question_bank[0].text)
print(question_bank[0].answer)

for i in range(len(question_bank)):
    print(f"{question_bank[i].text}.......{question_bank[i].answer}")



    
  


