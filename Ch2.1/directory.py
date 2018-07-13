from database import Simpledb as db

db = db('directory.txt')

while True:
    print('''
Type 'a' to add to the directory.
Type 'f' to find a name in the directory.
Type 'd' to delete a name in the directory.
Type 'u' to update a name in the directory.
Type 'q' to quit.
    ''')
    print()
    choice = input('Choose an option from above:\n')

    # When the add command is entered, the user should be prompted twice, first for a name (spaces allowed) and second for a phone number.
    # The name and number should be entered into the database with the name as the key and the number as the value.
    if choice == 'a':
        key = input('Enter the name to be added: ')
        value = input('Enter ' + key.title() + "'s phone number: ")
        db.insert(key, value)

    # When the find command is entered, the user should be prompted for a name, which the program then searches for.
    # If the name is found, the number should be printed; if it is not found, a message should say so.
    elif choice == 'f':
        key = input('Enter the name to be found: ')
        num = db.select_one(key)
        if num != None:
            print(key.title() + "'s number is " + num)
        else:
            print(key.title() + ' is not in the directory')

    # When the delete command is entered, the user should be prompted for a name, which the program then searches for.
    # If the name is found, the name and the phone number should be deleted. If the name is not found, a message should say so.
    elif choice == 'd':
        key = input('Enter the name to be deleted: ')
        key_found = db.delete(key)
        if not key_found:
            print('The entered name was not found in the directory')

    # When the update command is entered, the user should be prompted for a name, which the program then searches for.
    # If the name is not found, a message should say so.
    # If the name is found, the user should be prompted for the new phone number, which should replace the old phone number in the database.
    elif choice == 'u':
        key = input('Enter the name to be updated: ')
        is_in = db.select_one(key)
        if is_in == None:
            print('The name was not found in the directory')
        else:
            value = input('Enter an updated phone number for ' + key + ' : ')
            db.update(key, value)

    elif choice == 'q':
        break

    print("* * * * * * * * * * * * * * * * * * * * * ")


