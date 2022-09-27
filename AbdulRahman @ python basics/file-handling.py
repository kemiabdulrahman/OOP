# File Handling
f = open("C:/Users/AbdulRahman/empty-repo/AbdulRahman @ python basics/Kemi.txt", 'w')

f.write("Python is really Intresting as a Course")
f.close()
f = open("C:/Users/AbdulRahman/empty-repo/AbdulRahman @ python basics/Kemi.txt", 'r')

print(f.read())
f.close()
f = open("C:/Users/AbdulRahman/empty-repo/AbdulRahman @ python basics/Kemi.txt", 'a')
f.write("Hey, How is everything going, I hope you are doing well\n See You Later")
f.close()
p = open("C:/Users/AbdulRahman/empty-repo/AbdulRahman @ python basics/Kemi.txt", 'r')

p.read()

p.close()

import os
# os.remove("C:/Users/AbdulRahman/empty-repo/AbdulRahman @ python basics/Combined Basics.txt")
if os.path.exists("C:/Users/AbdulRahman/empty-repo/file-Deletion"):
    print("Valid")
    os.rmdir("C:/Users/AbdulRahman/empty-repo/file-Deletion")
else:
    print("Invalid Process")    

# print(f.read(5))

# f.close()






""" with open("C:/Users/AbdulRahman/empty-repo/AbdulRahman @ python basics/Combined Basics.txt", 'r') as f:

    for line in f:
        print(line, end='') 
    f_contents = f.readline()
    print(f_contents, end='')
    f_contents = f.readline()
    print(f_contents, end='') """

""" p = open('Combined Basics.txt', 'w')
p = open('Combined Basics.txt', 'a') """