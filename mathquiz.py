from random import randint
def main():
    askquestion()
def askquestion():
    firstvariable = randint(1,100)
    secondvariable = randint(1,100)
    question = "Add the following two numbers together "+ format(firstvariable) + " and " + format(secondvariable) +": "
    answer = int(input(question))
    verifyanswer(firstvariable, secondvariable, answer)
def verifyanswer(firstvarible,secondvariable, answer):
    realanswer = firstvarible + secondvariable
    if answer == realanswer:
        print("Congratulations you got the correct answer")
    else:
        print("Im sorry, the correct answer is", format(realanswer))
main()

