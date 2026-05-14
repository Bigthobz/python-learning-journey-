# Extract rows from the dataset
header = new_line_split[0]
data_row_1 = new_line_split[1]
data_row_2 = new_line_split[2]

# Store rows in a list
first_three = [header, data_row_1, data_row_2]

# Convert each row from string to list
index = 0

for each_string in first_three:
    first_three[index] = each_string.split(",")
    print(first_three[index])
    index += 1

# Print final nested list
print(first_three)