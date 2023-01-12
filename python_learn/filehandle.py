
# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist


f=open('C:\\Users\WELCOME\Documents\workhrs.txt', 'w')
f.write('''
EBS integration :
1. Validation Service(dev&test) - 8 hrs
2. Invoice Approval service(dev&test) - 9 hrs
3. PO & NON-PO invoice approval flow - 8 hrs

Codat Integration :
1. Supplier pull up and validation - 12 hrs
2. Customer pull up for invoice approval - 8 hrs
''')
f.close()
# for x in f:
#     print(x)
f=open('C:\\Users\WELCOME\Documents\workhrs.txt', 'r')
print(f.read())
f.close()

# print(f.readline())
# print(f.readline())


cr=open('newFile','x')
cr.close()

cr=open('newFile','a')
cr.write('Welcome to new file')
cr.close()

cr=open('newFile','r')
print(cr.read())
cr.close()



import os

os.remove('newFile')      #os built-in package used to remove file or folder in your system.

# os.rmdir('folder name') keyword for remove folder