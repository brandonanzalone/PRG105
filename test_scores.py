def main():
    test1 = int(input('Intput test score 1. '))
    test2 = int(input('Intput test score 2. '))
    test3 = int(input('Intput test score 3. '))
    test4 = int(input('Intput test score 4. '))
    test5 = int(input('Intput test score 5. '))
    average = calculate_average(test1, test2, test3, test4, test5)
    print("Your grade is a ",determine_grade(average))
def calculate_average(test1, test2, test3, test4, test5):
    average = (test1 + test2 + test3 + test4 + test5) / 5
    return average
def determine_grade(average):
    if average >= 90:
        return "A"
    else:
        if average >= 80:
            return "B"
        else:
            if average >= 70:
                return "C"
            else:
                if average >= 60:
                    return "D"
                else:
                    return "F"




main()
