#Python – Extract words starting with K in String List
userinput= input(" Enter your string in the list seperated by a comma:")
strlist=userinput.split(',')
print("List of strings is:",strlist)
k=input("Enter the character you want to extract the string from:")
new_strlist=[]
for i in strlist:
    if (i.startswith(k) or i.startswith(k.upper()) or i.startswith(k.lower())):
        new_strlist.append(i)
print("Your extracted strings with the letter is :",new_strlist)        