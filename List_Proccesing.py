import random
#main
def main():
    try:
        randomlist = randomizer()
        number = userinput()
        search(number, randomlist)
    except ValueError as e:
        print(e)
#random number generator
def randomizer():
    numbers = [0] * 20
    for index in range(20):
        numbers[index] = random.randint(1, 100)
    return numbers
#Takes the users input and checks if the input is valid
def userinput():
    number = input('Enter a numeral between 1 and 100. ')
    if not number:
         raise ValueError('Please enter a number between 1 and 100.')
    convertednumber = int(number)
    return convertednumber
#searches through the random numbers to find the user input
def search(number, randomlist):
    counter = 0
    for numberinlist in randomlist:
        if numberinlist > number:
            counter += 1
            print(numberinlist)
    if counter == 0:
        print("There are no numbers greater than ",number," in the list. ")
main()
