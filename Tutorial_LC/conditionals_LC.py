n = 1

if (n > 2):
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2
    
n, m = 1,2

if ((n > 2 and n != m) or n == m):
    n += 1
    
print("New Value of n:", n)
print(f"New Value of m: {m}")