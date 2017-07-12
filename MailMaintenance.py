import pickle
import os
def main():
    try:
        filename = 'emails.txt'
        currentdictionary = read_file(filename);
        selectedoption = present_options()
        name = input('Enter name ')
        if not name:
            raise ValueError('Please enter a name')
        if selectedoption == '1':
            searchresult = lookup_emailaddresses(name,currentdictionary)
            if not searchresult:
                print('No email found for', name)
            else:
                print(searchresult[1], 'was found for', name)
        elif selectedoption == '2':
            add_emailaddresses(name, currentdictionary)
        elif selectedoption == '3':
            update_emailaddresses(name, currentdictionary)
        else:
            delete_emailaddresses(name, currentdictionary)
        if len(currentdictionary) > 0:
            write_file(filename, currentdictionary)
    except ValueError as inputerror:
        print(inputerror)
    except IOError as fileerror:
        print('There was an error processing the file ', filename)
        #menu
def present_options():
        print('Select the operation you would like to perform')
        print('Enter 1 to Lookup an Email in the List')
        print('Enter 2 to Add an Email to the List')
        print('Enter 3 to Update and Email in the List')
        print('Enter 4 to delete and email')
        choice = input('Enter 1, 2, 3 or 4 ')
        if not choice or (choice != '1' and choice != '2' and choice != '3' and choice != '4'):
            raise ValueError('Please enter 1, 2, 3 or 4. ')
        return choice
#reads file
def read_file(filename):
    emaildictionary = {}
    if os.path.isfile(filename):
        file = open(filename, 'rb')
        emaildictionary = pickle.load(file)
    return emaildictionary

#writing from a file
def write_file(filename, currentdictionary):
    file = open(filename, 'wb')
    pickle.dump(currentdictionary,file)    
    
#adding emails
def add_emailaddresses(name, currentdictionary):
    email = input('Enter the email address you would like to add ')
    if not email:
            raise ValueError('Please enter an email address')
    currentdictionary[name] = email
    print(name , 'and this email',email, 'has been added to the list')
#looks for the email in the file
def lookup_emailaddresses(name, currentdictionary):
    for key, value in currentdictionary.items():
        if name.lower() == key.lower():
            return key, value
#updating the email
def update_emailaddresses(name, currentdictionary):
    searchresult = lookup_emailaddresses(name,currentdictionary)
    if not searchresult:
            print(name, 'Was not found in the list')
    else:
        question = 'Enter the new email address you would like to replace ' + searchresult[1] + ' '
        newemail = input(question)
        if not newemail:
                raise ValueError('Please enter an email address')
        currentdictionary[searchresult[0]] = newemail
    print(newemail , 'has been replaced for ', name)
#deleting the email
def delete_emailaddresses(name, currentdictionary):
    searchresult = lookup_emailaddresses(name,currentdictionary)
    if not searchresult:
        print(name, 'Was not found in the list')
    else:
        del currentdictionary[searchresult[0]]
    


main()
