#Opening a file in read mode
file = open('fruits.txt','r')

#Reading the entire file
content = file.read()
type(content) #Content returned is string

#Printing the contents of the file
print(content)

#Taking cursor back to start of file
file.seek(0)


#Reading content line by line
content = file.readlines()
type(content) #Content returned is a list
print(content)

#List comprehension to strip off \n
content = [i.rstrip('\n') for i in content]

for line in content:
    print(line)

#Important: Close the file
file.close()

