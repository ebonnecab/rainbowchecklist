#created a list 
checklist = list()

#create function 
def create(item):
    checklist.append(item)
    return checklist

#read function
def read(index):
    return checklist[index]
# print (checklist[0])

#update function
def update(index, item):
    checklist[index] = item
    return item
# print(checklist)

#delete function
def destroy(index):
    checklist.pop(index)

# def test():
#     create("purple sox")
#     create("red cloak")
#     update(0, "purple socks")
#     destroy(1)

# print(read(0))
# print(read(1))
# print(read(0))
# print(read(1)

