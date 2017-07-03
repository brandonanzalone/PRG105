
def main():
    try:
        fullname = input('Please enter you full name including middle name separated by spaces. ')
        if not fullname:
            raise ValueError('Please enter your full name separated by spaces. ')
        names = fullname.split(' ')
        if len(names) != 3:
            raise ValueError('Expecting first name middle name last name. ')
        findinitials(names)
    except ValueError as z:
        print(z)
#Takes full name and prints initials
def findinitials(names):
    initials = ""
    for name in names:
        initials += (name[0:1])
        initials += "."
    print(initials)
main()