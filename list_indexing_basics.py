# --- DATA ROWS ---
row_1 = ['Facebook', 'USD', 2974676, 3.5]
row_2 = ['Instagram', 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

# --- EXTRACT NAME, RATING COUNT, AND RATING ---
fb_data = [row_1[0], row_1[2], row_1[-1]]
insta_data = [row_2[0], row_2[2], row_2[-1]]
pandora_data = [row_5[0], row_5[3], row_5[-1]]

# --- DISPLAY EXTRACTED DATA ---
print(fb_data)
print(insta_data)
print(pandora_data)

# --- AVERAGE USER RATING ---
total_rating = row_1[-1] + row_2[-1] + row_5[-1]
avg_rating = total_rating / 3

# --- OUTPUT FINAL RESULT ---
print(int(avg_rating))
