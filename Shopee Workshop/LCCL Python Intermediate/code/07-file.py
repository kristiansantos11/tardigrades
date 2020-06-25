# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

# FILE
# ======================
print()

# METHOD 1 Open & Close
f = open('myfile', 'r')
print('File name:', f.name)
print('Mode:', f.mode)
f.close()

print()

# METHOD 2 Open & Close
#with open('myfile', 'r') as f:
    # Reading a file
    # content = f.read()        # returns a string
    # content = f.read(50)      # returns a string
    # content = f.readlines()   # returns a list
    # content = f.readline()    # returns a string

    # print(content)

    #for line in f:
    #    print('Line:', line, end='')


# # Writing to file
with open('newfile', 'w') as f:
     f.write('hello\n')
     f.write('world')
     f.seek(0)
     f.write('begin')
     f.write('begin')


# # Appending to file
with open('newfile', 'a') as afile:
     afile.write('bye')


print()