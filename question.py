class Question:
      def __init__(self,text,answer):
        self.text = text
        self.answer= answer

new_quest = Question("Who is the CM of Kerala","Biriyani")
print(new_quest.text,"\n",new_quest.answer)