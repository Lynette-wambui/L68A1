# Step 1: Ask the user for the base number
base = int(input("Enter the base number: "))

# Step 2: Ask the user for the exponent(power)
exp = int(input("Enter the power: "))

# Step 3: Start result as 1 (because multiplying by 1 doesn't changre the number)
result = 1

# Step 4: Multiply the base 'exp' number of times
for i in range(exp):
    print("Step", i + 1, ":", result, "*", base) # Showeach step
    result = result * base

# Step 5: Show the final result
print("\nFinal Answer: ")
print(base, "to the power", exp, "is", result) 