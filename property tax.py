def main():
    value = float(input('What is the actual total value of your property? '))
    cost = value * .6
    print("Your assessed value is $",format(cost,'.2f'))
    calculate_cost(cost)
def calculate_cost(cost):
    print("Your tax on the land is $",format(cost / 100 * .72,'.2f'))


main()
