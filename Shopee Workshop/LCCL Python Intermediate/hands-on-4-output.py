


vowels = 'aeiou'
c = 0
v = 0

with open('myfile', 'w') as f:
    f.write("Whoops. I have replaced the content\n")
    f.write("This was written using write mode.")
    f.close()

with open('myfile', 'r') as f:
    a = f.read()
    for i in a.lower().replace('.', '').split():
        if i[0] in vowels:
            v += 1
        else:
            c += 1
    f.close()

print(f"Words that start with consonants: {c}")
print(f"Words that start with vowels: {v}")
