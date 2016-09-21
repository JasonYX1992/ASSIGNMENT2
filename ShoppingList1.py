import csv


def required_list():  # Build a required list
    if L1:            # If the list is not empty
        s = 0
        v = 0
        sort_func(L1)  # Build a sorted list according to the priority
        List1 = []
        for i in L1:
            s += float(i[1])  # Add up and sum the total number
            List1.append('{0}. {1}         $  {2:.2f} ({3})'.format(v, i[0], float(i[1]), i[2]))
            v += 1
        return List1, 'Total expected price for {0} items: ${1:.2f}'.format(len(L1), s)
    else:
        return 'No completed items'
        

def completed_list():  # Build a completed list
    if L2:             # If the list is not empty
        s = 0
        v = 0
        sort_func(L2)  # Build a sorted list according to the priority
        List2 = []
        for i in L2:
            s += float(i[1])  # Add up and sum the total number
            List2.append('{0}. {1}         $  {2:.2f} ({3})'.format(v, i[0], float(i[1]), i[2]))
            v += 1
        return List2, 'Total expected price for {0} items: ${1:.2f}'.format(len(L2), s)
    else:
        print('No completed items')


def mark_list():  # Build a mark list
    if L1:        # If the list is not empty
        required_list()  # List the required list first
        v_list = list(range(len(L1)))  # Get the number range
        print('Enter the number of an item to mark as completed')
        while True:  # Loop input corresponding index value of the marked item
            v = input('>>> ')  # Input corresponding index value of the marked item
            if v.isdigit():  # If is a number
                if int(v) in v_list:  # If the number is in the range
                    v = int(v)
                    item = L1[v]
                    print('{0} marked as completed'.format(item[0]))
                    L1.pop(v)   # Delete the marked item from the list
                    item[-1] = 'c'  # Change the marked item
                    L2.append(item)  # Append the marked item into completed list
                    break
                else:
                    print('Invalid item number')
            else:                   # If not a number
                print('Invalid input; enter a number')
    else:
        print('No required items')


def add_item():  # Build a add item
    while True:  # Loop input the item name
        item_name = input('Item name:')
        if not item_name.isspace():  # If the input is not blank
            break
        else:
            print('Input can not be blank')

    while True:            # Loop input the item price
        price = input('Price: $')
        if price.isdigit():  # If the input is a number
            break
        elif price[0] == '-' and price[1:].isdigit():  # If the value is negative
            print('Price must be >= $0')
        else:
            print('Invalid input; enter a valid number')

    while True:     # Loop input the item priority
        priority = input('Priority:')
        if priority.isdigit():  # If the input is a number
            if priority in '123':  # If the priority is in the range
                break
            else:
                print('Priority must be 1, 2 or 3')
        else:
            print('Invalid input; enter a valid number')

    print('{0}, ${1} (priority {2}) added to shopping list'.format(item_name, price, priority))
    L1.append([item_name, price, priority, 'r'])        # Save the append item
    

def sort_func(L):  # Sort function
    L.sort(key=lambda i: int(i[2]), reverse=False)    # Build a sorted list according to the priority
    return L


def writer_csv(L):     # write the data into csv file
    cs = open('items.csv', 'w', newline='')   # open the csv file
    wr = csv.writer(cs)
    wr.writerows(L)


def menu():
    print('''
Shopping List 1.0 - by {0}
{1} items loaded from items.csv'''.format('YangXing', len(L1)))
    while True:
        print(
'''Menu:
R - List required items 
C - List completed items
A - Add new item
M - Mark an item as completed
Q - Quit
>>> ''', end='')
        
        items = input().lower()  # Transfer input to lowercase
        if items in 'rcamq':
            if items == 'r':
                required_list()
            elif items == 'c':
                completed_list()
            elif items == 'a':
                add_item()
            elif items == 'm':
                mark_list()
            elif items == 'q':
                print('''{0} items saved to items.csv
Have a nice day :)'''.format(len(L2)))
                writer_csv(L2)  # Add new data into items.csv
                break
        else:
            print('Invalid menu choice')

# Read the data from csv file and sorted:
# global L1,L2
csvfile = open('items.csv', newline='')  # Open the csv_file
L1 = list(csv.reader(csvfile))      # Read the data
# print(L1)
csvfile.close()
L2 = []   # Initial the completed item list

# Call the menu function
#menu()


