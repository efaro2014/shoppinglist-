import os

shopping_list = []

def clear_screen():
    os.system = ('cls')

def show_help():
    clear_screen()
    print('what are we going to buy today? ')
    print("""
         Enter 'DONE to End shopping 
         Enter  'HELP' to see the Help menu
         Enter 'SHOW' to see the shopping list 
         Enter 'REMOVE' to remove an item from the list""")

def adding_list(item):
    show_list()
    if len(shopping_list):
        position = input('Where should I put the {}? \n'
                         'Press in Enter to add to the end of the list\n'
                         '>'.format(item))
    else:
        position = 1
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position - 1, item)
    else:
        shopping_list.append(new_item)
    print('You have {} items!'.format(len(shopping_list)))
    show_list()

def show_list():
    clear_screen()
    print('Here is your list')
    for index, item in enumerate(shopping_list, start = 1):
        print(index, item)
    print('-' * 10 )

def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove? >  ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        print("Oh sorry {} is not in the list please try again".format(what_to_remove))
    show_list()
show_help()
while True:
    new_item = input("> ")
    if new_item.upper() == "DONE":
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list()
        continue
    adding_list(new_item)


show_list()

