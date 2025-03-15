# Full program to analyze time complexity
n = int(input("Enter the value of n: "))

# First loop
for i in range(0, n+1):
    print("first loop")
    
# Fixed while loop
j = 1
while j <= n+1:
    print("2nd loop", j)
    j += 1  # Increment j to prevent infinite loop

# Second loop
for i in range(0, 100):
    print("3rd loop")
