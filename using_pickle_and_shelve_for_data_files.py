import pickle
import shelve

#~~~~~~~~~~~~~~~~PICKLE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
outfile = open('data.txt', 'wb')
letters = ['j','o','r','d','a','n']
dumped = pickle.dump(letters, outfile)
outfile.close()


infile = open('data.txt', 'rb')
file_data = pickle.load(infile)
infile.close()

#~~~~~~~~~~~~~~~~SHELVE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

db_file = shelve.open('letters.txt', 'c')
db_file['vowels'] = ['a', 'e', 'i', 'o', 'u']
db_file['end'] = ['x', 'y', 'z']
db_file.close()

db_file = shelve.open('letters.txt', 'c')
print(list(db_file.keys()))

print('vowels' in db_file)

del db_file['vowels']

print('vowels' in db_file)

db_file.close()
