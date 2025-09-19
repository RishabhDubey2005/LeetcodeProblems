# Division is decimal by default
print(5 / 2) # Output: 2.5

# Double slach rounds down to an intger:
print(5 // 2) # Output: 2

print()

# Issues with negative values:
print(-3 // 2) # Output: -2

print()

# Solution around negative values:
print(int(-3 / 2)) # Use decimal division and parse as an int

print()

# Modulo Operator:
print(10 % 3)

print()

# Negative Values Operator Problem:
print(-10 % 3)

print()

# Solution: Import math library and use the fmod function:
import math
print(math.fmod(-10, 3))

print()

# Math Helpers:
print(math.floor(3 / 2)) # Will Round the Value Down

print()

print(math.ceil(3 / 2)) # Will Round the Value Up

print()

print(math.sqrt(2)) # Will take the square root of the value

print()

print(math.pow(2, 3)) # Will take the power of the given number and the exponent (2^3)

print()

# Getting the MAX int:
float("inf")

# Getting the MIN int:
float("-inf")

# Python numbers are infinte so they never overflow
print(math.pow(2, 200)) # Won't print the precise number of the operation

print()

# But still less than infinity:
print(math.pow(2, 200) < float("inf"))

