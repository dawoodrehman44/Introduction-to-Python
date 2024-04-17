print("Hello world")

# Writing first dictionary
this_dic = {
    "brand" : "Ford",
    "model" : "Mustan",
    "year" : 1964

}
print(this_dic)

##############################################################################################
# Creating a dictionary
student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science"
}

# Accessing values in the dictionary
print(student["name"])  # Output: John
print(student["age"])   # Output: 20

# Modifying a dictionary
student["age"] = 21  # Modify value
student["year"] = 3  # Add new key-value pair
del student["major"] # Remove a key-value pair

# Printing the modified dictionary
print(student)
##############################################################################################
# Creating a dictionary
student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science"
}

# Printing the original dictionary
print("Original Dictionary:", student)

# Using keys() function to get all keys
print("Keys in the dictionary:", student.keys())

# Using values() function to get all values
print("Values in the dictionary:", student.values())

# Using items() function to get key-value pairs
print("Key-Value pairs in the dictionary:", student.items())

# Using get() function to retrieve value by key
print("Value for key 'name':", student.get("name"))

# Using update() function to add or update items from another dictionary
student.update({"age": 21, "year": 3})
print("Updated Dictionary:", student)

# Using pop() function to remove item by key
removed_item = student.pop("major")
print("Removed Item:", removed_item)
print("Dictionary after removing 'major':", student)

# Using clear() function to remove all items from the dictionary
student.clear()
print("Dictionary after clearing all items:", student)
##############################################################################################
