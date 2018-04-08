#Opening file in write mode
file = open('write_sample.txt','w')

#Wrting content onto file directly
file.write("Hello World\nThis is a python class\nAlbertech rocks")

file.close()

#Opening another file to write from a string
file = open('string_write.txt','w')
content = '''Hello Guys,
How are you all doing?
Let's make some noise for Pyty Boys
'''
file.write(content)

file.close()

#Opening another file to write from a list
file = open('list_write.txt','w')
lst = ["This is line1\n","This is line2\n", "This is line3\n"]

for line in lst:
    file.write(line)

file.close()