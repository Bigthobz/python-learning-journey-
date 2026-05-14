from csv import reader

# Open the file
opened_file = open('AppleStore.csv')

# Read the file using csv reader
read_file = reader(opened_file)

# Convert to list of lists
apps_data = list(read_file)

# Close the file
opened_file.close()

# --- BASIC CHECKS ---
print(len(apps_data))     # total rows
print(apps_data[0])       # header row
print(apps_data[:3])      # first 3 rows