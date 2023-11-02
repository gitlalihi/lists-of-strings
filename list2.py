#Python code to demonstrate  to Reverse All Strings in String List
userinput= input(" Enter your string in the list seperated by a comma:")
strlist=userinput.split(',')
print("List of strings is:",strlist)
for i in strlist:
    rev_string =[i[::-1]]
print("Your reversed string in the list is:",rev_string)    