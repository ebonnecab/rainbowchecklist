#created a list 
checklist = list()

#create function 
def create(item):
    checklist.append(item)
   

#read function
def read(index):
    return checklist[index]

#update function
def update(index, item):
    checklist[index] = item
# print(checklist)

#delete function
def destroy(index):
    checklist.pop(index)

#for loop
def list_all_items():
    index = 0
    for list_item in checklist:
        print("Index: {} Item: {}".format(index, list_item))
        index += 1


# select function
def select(function_code):


# create item
    if function_code == "C":
        create_item = input("Input item: ")
        create(create_item)

# read item
    elif function_code == "R":
        index = int(input("Which item number do you want view from the list? You only have {}: ".format(len(checklist))))
        read(index)

#print all items
    elif function_code == "P":
        list_all_items()

#destroys item
    elif function_code == "D":
        index = int(input("Which item number do you want to destroy from the list? You only have {}: ".format(len(checklist))))
        destroy(index)

#quit
    elif function_code == "Q":
        print('now exiting...')
        return False

    else:
        #Catch all
        print("Unknown Option")
        return True

# user input
def user_input(prompt):
        # the input function will display a message in the terminal
        # and wait for user input.
        user_input = input(prompt)
        return user_input

#while loop
running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, and P to display list. Press Q to quit.")

    running = select(selection)
  

# test
def test():

    create("purple sox")
    create("red cloak")
    print(read(0))
    print(read(1))
    update(0, "purple socks")
    destroy(1)
    print(read(0))
    select("C")
    list_all_items()
    select("R")
    list_all_items()
    select("P")
    list_all_items()
    select("D")
    list_all_items()
    select("Q")
    
    # user_value = user_input("Please Enter a value:")
    # print(user_value)
test()

