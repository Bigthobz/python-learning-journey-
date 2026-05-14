from csv import reader

# Open and read file
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

# --- COLLECT ALL RATINGS ---
all_ratings = []

for row in apps_data[1:]:  # skip header
    rating = float(row[7])
    all_ratings.append(rating)

# --- CALCULATE AVERAGE ---
avg_rating = sum(all_ratings) / len(all_ratings)

print(avg_rating)