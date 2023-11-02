#Python – Way to remove multiple empty spaces from string List
userinput = input("Enter your string:").split()  
newlist = []

for i in userinput:
    newlist.append(i.strip())  
print("Your strings after removing empty spaces are:", newlist)