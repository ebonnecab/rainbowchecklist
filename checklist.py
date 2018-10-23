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

# mark completed function
# def mark_completed(index):
    


