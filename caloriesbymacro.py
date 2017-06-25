calories = 0
def main():
    fat()
    carbs()
    protien()
    total()
def fat():
    global calories
    fatgrams = int(input('What was the amount of fat consumed today? '))
    calories += fatgrams * 9
    print("Calories from fat", calories)
def carbs():
    global calories
    carbgrams = int(input('What was the amount of fat consumed today? '))
    calories += carbgrams * 4
    print("Calories from carbs",calories)
def protien():
    global calories
    protiengrams = int(input('What was the amount of fat consumed today? '))
    calories += protiengrams * 4
    print("Calories from protien",calories)
def total():
    global calories
    print("Total calories for the day is", calories)
main()
