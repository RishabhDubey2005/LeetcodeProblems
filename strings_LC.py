# String are similar to arrays/lists
# Can use single or double quotes
s = "abc"
print(s[0:2]) # Splice them the same way as lists

# Strings are IMMUTABLE:
# s[0] = "A" # Will NOT WORK

# Instead, update/reassign a new value to the string:
s += "def"
print(s)

# String can be converted into integers:
print(int("123") + int("123"))

# And numbers can be converted into strings:
print(str(123) + str(123))

# Use the ASCII value of a char by using the ord function
print(ord("A"))
print(ord("4"))

# Combine a list of string (with an empty string using a DELIMETER): use the join method
string = ["ab", "cd", "ef"]
print("".join(string)) # Appending the empty string together

print("4".join(string)) # Adds a 4 after each element in the list, except for the last entry