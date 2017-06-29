# main function
def main():
    total = 0.0
    counter = 0.0
    try:
# opening and displaying the file
        f = open("c:\\numbers.txt", "r")
        for line in f:
            counter += 1
            try:
                total += int(line)
            except ValueError as b:
                print(b)
        print("Total average of numbers is ", format(calculate_average(total, counter),'.2f'))
    except IOError as e:
        print(e)
def calculate_average(total, counter):
    average = 0.0
    average = total / counter
    return average
    print()
main()
