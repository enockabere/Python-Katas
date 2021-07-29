# Create the popular Magic 8 Ball game. If you've never played it before,
# it is a toy that you can ask a yes-or-no question and it will give you a
# random answer (feel free to read more on the Wikipedia page).
import random
def magicBall():
    quiz = input ("Ask me anything?\n")
    answer = ["It is Certain","As I see it, yes","Reply hazy, try again.","Don't count on it"]
    rand = random.randint(0,4)
    if rand == 1:
        print(answer[1])
    elif rand == 2:
        print(answer[2])
    elif rand == 3:
        print(answer[3])
    elif rand == 4:
        print(answer[4])
    else:
        print("Too hard!, I don't know")
magicBall()
    
