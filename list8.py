#Python program to Replace all Characters of a List Except the given character
userinput= input(" Enter your string in the list seperated by a comma:")
strlist=userinput.split(',')
print("List of strings is:",strlist)
repchar=input("Enter the character you want to replace with:")
retainchar=input("Enter the chracters you want to retain: ")
new_strlist=[]
for i in strlist:
    modified_string = i.replace(repchar,retainchar)
    new_strlist.append(modified_string)
print("Your Modified list is",new_strlist)