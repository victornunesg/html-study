# ----------------------------
# FILE HANDLING - READING FILES
# ----------------------------

# opening a file in 'read only' mode
my_file = open('greeting.txt', 'r')  # there also are w(write) and a(append) options for this parameter

# reading the hole file
# print(my_file.read())

# reading 10 first characters of the file
#print(my_file.read(10))

# reading the first and second line of the file
#print(my_file.readline())
#print(my_file.readline())

# printing all the lines individually of the document, in two equivalent ways:
line_by_line = my_file.readlines()
line_by_line1 = my_file.read().splitlines()
print('readlines: ', line_by_line)
print('splitlines: ', line_by_line1)

# always close the file after
my_file.close()

with open('friends.csv', 'r') as f:
    print(f.read())
    friends = f.read().splitlines()
    print(friends)
