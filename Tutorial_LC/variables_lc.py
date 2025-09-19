# Dynamic Variables:
n = 0
print("n = ", n)

n = "abc"
print("n = ", n)

# Multiple Assignments:
n, m = 0, "abc"

n, m, z = 0.125, "abc", False #Okay to have variables with different data types 

# Increment:
n = n + 1 # Good
n += 1 # Also good
#n++ BAD

# None is null (absence of value):
n = 4
n = None # Equivalent to Null in Java
print("n: ", n)