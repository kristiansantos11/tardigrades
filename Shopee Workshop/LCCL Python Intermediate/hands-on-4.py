# Hands on 4

# Write a program that reads a Python file. The program removes comments from the
# input file and output the same Python program without comments. Ignore cases where
# comments appear in a string.

count = 0
with open('hands-on-3.py', 'r') as fin:
    with open('hands-on-4-output.py', 'w') as fout:
        for line in fin:
            i = line.find("#")
            if i > 0:
                fout.write(line[:i] + '\n')
            elif i == 0:
                continue
            else:
                fout.write(line)
