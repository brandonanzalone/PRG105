def main():
    loan = float(input('What is your monthly loan payment for your vehicle? '))
    insurance = float(input('What is your monthly insurance payment for your vehicle? '))
    gas = float(input('What is your monthly gas expense for your vehicle? '))
    oil = float(input('What is your monthly oil expense for your vehicle? '))
    tires = float(input('What is your monthly tires expense for your vehicle? '))
    maintenance = float(input('What is your monthly maintenance expense for your vehicle? '))
    cost = loan + insurance + gas + oil + tires + maintenance
    print("Your monthly automobile costs are $",format(cost,'.2f'))
    calculate_cost(cost)
def calculate_cost(cost):

    print("Your annual automobile costs are $",format(cost * 12,'.2f'))


main()
