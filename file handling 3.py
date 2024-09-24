#program to count number of lines in this file
#opening a file 
file = open('Codingal.txt','r')
counter = 0 

# reading from file
Content = file.read()
# splitting content into lines
# and storing them in a list
CoList = Content.split("\n")

for i in CoList:
         if i:
                  counter += 1

print("This is the number of lines in the file")
print(counter)