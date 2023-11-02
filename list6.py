#Python – Split String of list on K character
userinput= input(" Enter your string in the list seperated by a comma:")
strlist=userinput.split(',')
print("List of strings is:",strlist)
k=input("Enter the character you want to split the string from:")
new_strlist=[]
for i in strlist:
    x=i.split(k)
    new_strlist.extend(x)
new1strlist=','.join(new_strlist)    
print("Your split strings with the letter is :",new1strlist)        