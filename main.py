# Show the Fun Title
print(r""" 
    ______                         __            _                    __    __
   / ____/   _  __  _____  ___    / /   _____   (_)  ____    _____   / /   / /
  / __/     | |/_/ / ___/ / _ \  / /   / ___/  / /  / __ \  / ___/  / /   / / 
 / /___    _>  <  / /__  /  __/ / /   (__  )  / /  / /_/ / / /     /_/   /_/  
/_____/   /_/|_|  \___/  \___/ /_/   /____/  /_/   \____/ /_/     (_)   (_)   
                                                                              


""")
#Introduce the user to the test!!!!
print("Welcome true belivers!!! today marks the first ever Marvel 'MCU' fan super quiz!!!!: ")
print()
# create questions and answers for the super fan!! 
questions = "Q1. Is Iron man the first Avenger?", "Q2. Was Red Skull the ferryman on vormir?", "Q3. Did spider man join iron man in Germany?"
answers = "F", "T", "T"
userAnswer = " "
#tools that will help us later :) 
numberOfQuestions = len(questions)
userAnswer = " " 
count = 0

#Create a loop to show each question on their own iteration 
for index in range(numberOfQuestions): 
  print(questions[index])
  print(answers[index])
  print()
  userAnswer = answers 
  count = 1
  