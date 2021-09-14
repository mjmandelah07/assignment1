# : Given a string, display only those characters which are present at an even index number

name = input("Enter a word: ")
for a in range(1, len(name)-1, 2):
    print("index[", a, "]", name[a])
