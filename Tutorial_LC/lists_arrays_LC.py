# Arrays and Lists are the SAME thing in Python
arr = [1,2,3]
print(arr)

# Lists/Stacks can be used as a Stack:
arr.append(4)
arr.append(5)
print(arr) # 1, 2, 3, 4, 5

arr.pop() # Will remove the last most element from the list Output: 1,2,3,4
print(arr)

# Can insert values anywhere in the list:
arr.insert(1,7) # Inserts element 7 at index 1
print(arr)

arr[0] = 0
arr[3] = 0
print(arr)

# Initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# Indexing -1 to read the last value:
print(arr[-1])

# Indexing -2 to read the second to last value:
print(arr[-2])

# Sublists (Slicing):
arr = [1,2,3,4]
print(arr[1:3]) # Taking value from index 1-3 but NOT including index 3: 1 -> 3 - 1
print(arr[0:4])

#Unpacking
a, b, c = [1,2,3] # Make sure the number of variables match the expected number of elements in an array on the right
print(a,b,c)

# Loop through arrays/lists:
nums = [1,2,3]

# For Loop using INDEX:
for i in range(len(nums)):
    print(nums[i])

print()

# For Loops Without INDEXING:
for i in nums:
    print(i)

print()    

# For Looping with index and value:
for i, n in enumerate(nums):
    print(i, n)
    
print()

# Loop through multiple arrays sim. with unpacking:
nums1 = [1,3,5]
nums2 = [2,4,6]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
    
print()

# Reversing an array:
nums = [1,2,3]
print(nums.reverse)

# Sorting an array:
arr = [5,4,7,3,8]
arr.sort()
print(arr)

arr.sort(reverse = True) # Sort the array in reverse order
print(arr)

# Can also sort a string of lists:
arr = ["bob", "alice", "jane", "doe"] # Sorted based on alphabetical order
arr.sort()
print(arr)

# Custom Sort (by length of string):
arr.sort(key=lambda x: len(x))
print(arr)