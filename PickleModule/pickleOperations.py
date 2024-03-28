import pickle

li = ['a', 'b', 'c', 'd', 'e']
with open('data.txt', 'wb') as file:
    pickle.dump(li, file)

with open('data.txt', 'rb') as file:
    desrlzed = pickle.load(file)

print(desrlzed)
