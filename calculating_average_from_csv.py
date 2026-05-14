from csv import reader

# Open the file
opened_file = open('AppleStore.csv')

# Read CSV file
read_file = reader(opened_file)

# Convert to list
apps_data = list(read_file)

# Close file
opened_file.close()

# --- CALCULATE TOTAL RATINGS ---
rating_sum = 0

for row in apps_data[1:]:  # skip header
    rating = float(row[7])
    rating_sum += rating

print(rating_sum)

# --- CALCULATE AVERAGE RATING ---
avg_rating = rating_sum / 7197

print(float(avg_rating))