opened_file = open('AppleStore.csv')
read_file = opened_file.read ()
print (read_file[:300])
opened_file.close()