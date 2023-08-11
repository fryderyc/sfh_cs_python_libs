# String manipulation
my_string = "This is a string."
print(my_string)

# Tuples (immutable sequence)
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# Lists (mutable sequence)
my_list = ["dog", "cat", "elephant"]
print(my_list)

# Sets (collection of unique elements)
my_set = {"apple", "banana", "cherry"}
print(my_set)

# Dictionaries (key-value pairs)
my_dict = {"name": "John", "age": 25, "occupation": "developer"}
print(my_dict)

# Accessing elements from different data types
print(my_string[2])  # Accessing individual characters
print(my_tuple[0])  # Accessing elements in a tuple
print(my_list[2])  # Accessing elements in a list
print("banana" in my_set)  # Checking if an element exists in a set
print(my_dict["name"])  # Accessing value by key in a dictionary

# Modifying elements in lists
my_list[2] = "tiger"
print(my_list)

# Adding elements to sets
my_set.add("dragonfruit")
print(my_set)

# Updating values in dictionaries
my_dict["age"] = 26
print(my_dict)