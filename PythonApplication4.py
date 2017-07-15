from Person import Person


def main():
    personalcollection = []
    #try catch for user input
    try:
        personalcollection = collect_personal_information()
        for currentperson in personalcollection:
            print("first name:", currentperson.get_name())
            print("Address:", currentperson.get_address())
            print("Age:", currentperson.get_age())
            print("Phonenumber:", currentperson.get_phonenumber())
    except ValueError as a:
        print(a)
#function to collect personal informationd
def collect_personal_information():
    personalcollection = []
    while len(personalcollection) < 3:
        name = input('What is your name? ')
        if not name:
            raise ValueError('Please enter a name. ')
        address = input('What is your address? ')
        if not address:
            raise ValueError('Please enter an address. ')
        age = input('How old are you? ')
        if not age:
            raise ValueError('Please enter an age. ')
        phonenumber = input('What is your phonenumber? ')
        if not phonenumber:
            raise ValueError('Please enter a phonenumber. ')
        personalcollection.append(Person(name,age, address, phonenumber))
    return personalcollection
        
main()
