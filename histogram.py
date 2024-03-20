file = open("casmurro.txt", 'r')

for line in file:
    for word in line.split():
        print(word)

        