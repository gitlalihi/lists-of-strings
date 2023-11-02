#Python – Split Strings on Prefix Occurrence
userinput= input(" Enter your string in the list seperated by a comma:")
strlist=userinput.split(',')
print("List of strings is:",strlist)
k=input("Enter the prefix you want to split the string from:")
new_strlist=[]
new1_strlist=[]
for i in strlist:
    if i.startswith(k):
       if new1_strlist:
          new_strlist.append(new1_strlist)
       new1_strlist=[i]
    else:
       new1_strlist.append(i)
if new1_strlist:  
    new_strlist.append(new1_strlist)

print("Prefix Split List : " ,new_strlist)