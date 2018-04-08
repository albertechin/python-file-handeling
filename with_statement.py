#Working on file using with block for cleaner code + no need close the file explicitly
with open('fruits.txt','a+') as file:
    #Bringing cursor to the beginning of the file
    file.seek(0)

    #Reading from the file
    print("File before updation:")
    content = file.read()
    print(content)

    #Appending the file
    file.write("Peech\n")


