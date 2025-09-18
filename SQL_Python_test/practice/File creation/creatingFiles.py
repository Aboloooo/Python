#Creating an empty file
# f = open("secondFile.text" , "x")
counter = 0
while True:
    counter = counter+1
    open(f"{counter}_test.text", "x")
    if counter == 2:
        break