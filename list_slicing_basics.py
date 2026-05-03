# --- DATA ROWS ---
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

# --- LIST SLICING ---
first_4_fb = row_1[:4]      # first 4 elements
last_3_fb = row_1[-3:]      # last 3 elements
pandora_3_4 = row_5[2:4]    # elements at index 2 and 3

# --- OUTPUT RESULTS ---
print(first_4_fb)
print(last_3_fb)
print(pandora_3_4)
