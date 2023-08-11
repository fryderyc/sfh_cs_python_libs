# Opening a file in read mode
file = open("example.txt", "r")

# Reading the contents of the file
content = file.read()
print(content)

# Closing the file
file.close()

# Opening a file in write mode
file = open("new_file.txt", "w")

# Writing to the file
file.write("Hey there, this is some text.")
file.write("I'm loving this file handling.")

# Closing the file
file.close()

# Opening a file in append mode
file = open("new_file.txt", "a")

# Appending additional content to the file
file.write("Adding more text to the file.")

# Closing the file
file.close()

# Opening a file in read mode once again
file = open("new_file.txt", "r")

# Reading and printing the updated contents of the file
updated_content = file.read()
print(updated_content)

# Closing the file
file.close()