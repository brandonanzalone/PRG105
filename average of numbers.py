def main():
    total = 0.0
    counter = 0.0
    f = open("c:\\numbers.txt", "r")
    for line in f:
        counter += 1
        total += int(line)
    print("Total average of numbers is ", format(calculate_average(total, counter),'.2f'))
def calculate_average(total, counter):
    average = 0.0
    average = total / counter
    return average
    print()
main()
