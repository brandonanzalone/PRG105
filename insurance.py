def main():
    cost = float(input('What is the cost to replace the building? '))
    calculate_cost(cost)
def calculate_cost(cost):
    amount = cost * .8
    print("Minimum insurance is $",format(amount,'.2f'))


main()

