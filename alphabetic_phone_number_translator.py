
def main():
    try:
        phonenumber= input('Please enter Phone number in the format XXX-XXX-XXXX. ')
        if not phonenumber:
            raise ValueError('Please enter phone number in the following format XXX-XXX-XXXX. ')
        phoneparts = phonenumber.split('-')
        if len(phoneparts) != 3:
            raise ValueError('Expecting phone number in the following format XXX-XXX-XXXX. ')
        if len(phoneparts[0]) != 3 or len(phoneparts[1]) != 3 or len(phoneparts[2]) != 4:
            raise ValueError('Expecting phone number in the following format XXX-XXX-XXXX. ')
        parsephonenumberstring(phoneparts)
    except ValueError as z:
        print(z)
#takes phonenumber and parse and translate
def parsephonenumberstring(phoneparts):
    counter = 0
    translatedphonenumber = ""
    for part in phoneparts:
        for character in part:
            if character.isalpha():
                translatedphonenumber += translatelettertonumber(character)
            elif character.isnumeric():
                translatedphonenumber += character
            else:
                raise ValueError('This character is not alpha or numeric. ', character)
        counter += 1
        if counter < 3:
            translatedphonenumber += '-'
    print(translatedphonenumber)
#translate letter to the corresponding phone number
def translatelettertonumber(character):
    number2 = ['A', 'B', 'C']
    number3 = ['D', 'E', 'F']
    number4 = ['G', 'H', 'I']
    number5 = ['J', 'K', 'L']
    number6 = ['M', 'N', 'O']
    number7 = ['P', 'Q', 'R', 'S']
    number8 = ['T', 'U', 'V']
    number9 = ['W', 'X', 'Y', 'Z']
    if character.upper() in number2:
        return '2'
    elif character.upper() in number3:
        return '3'
    elif character.upper() in number4:
        return '4'
    elif character.upper() in number5:
        return '5'
    elif character.upper() in number6:
        return '6'
    elif character.upper() in number7:
        return '7'
    elif character.upper() in number8:
        return '8'
    else:
        return '9'


main()