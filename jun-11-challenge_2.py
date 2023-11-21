# Read the input from input_2.txt
with open('input_2.txt', 'r') as file:
    content = file.read().split()

# Parse the integers
num1 = int(content[0])
num2 = int(content[1])

# Calculate the sum and difference
sum_result = num1 + num2
diff_result = abs(num1 - num2)

# Write the results to output_2.txt
with open('output_2.txt', 'w') as file:
    file.write(str(sum_result) + ' ' + str(diff_result))