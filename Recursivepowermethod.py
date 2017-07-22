def main():
    print('8 to the power of 8 ',str(power(8,8)))
#recursive function
def power(number, exponent):
    if exponent == 0:
        return 1
    else:
        return number * power(number, exponent-1)
main()

