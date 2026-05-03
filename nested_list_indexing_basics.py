# --- DATA ROWS ---
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

# --- DATASET (LIST OF LISTS) ---
app_data_set = [row_1, row_2, row_3, row_4, row_5]

# --- EXTRACT RATINGS ---
row_1_rating = app_data_set[0][-1]
row_2_rating = app_data_set[1][-1]
row_3_rating = app_data_set[2][-1]
row_4_rating = app_data_set[3][-1]
row_5_rating = app_data_set[4][-1]

# --- PRINT RATINGS ---
print(row_1_rating)
print(row_2_rating)
print(row_3_rating)
print(row_4_rating)
print(row_5_rating)

# --- AVERAGE RATING ---
avg_rating = (
    row_1_rating +
    row_2_rating +
    row_3_rating +
    row_4_rating +
    row_5_rating
) / 5

print(avg_rating)
