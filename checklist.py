#created a list 
checklist = list()

#create function 
def create(item):
    checklist.append(item)
    return checklist

#read function
def read(index):
    return checklist[index]

#update function
def update(index, item):
    checklist[index] = item
    return item
# print(checklist)

#delete function
def destroy(index):
    checklist.pop(index)
# test
def test():
    create("purple sox")
    create("red cloak")
    print(read(0))
    print(read(1))
    update(0, "purple socks")
    destroy(1)
    print(read(0))
test()

#for loop
def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1
        print("{} {}".format(index, list_item))
list_all_items()

# select function
def select(function_code):

# create item
    if function_code == "C":
        create_item = input("Input item: ")
        create(create_item)
        print(checklist)

# read item
    elif function_code == "R":
        index = int(input("Which item number do you want from the list? You only have {}: ".format(len(checklist))))
        print(read(index))
    
select("R")


