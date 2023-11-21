# Read input from input_1.txt
with open('wangda-input-sample.py', 'r') as input_file:
    str1 = input_file.readline().strip()
    str2 = input_file.readline().strip()

# Concatenate the strings
concatenated_string = str1 + str2

# Write the concatenated string to output_1.txt
with open('output_1.txt', 'w') as output_file:
    output_file.write(concatenated_string)