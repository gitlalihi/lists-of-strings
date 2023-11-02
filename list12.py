#Python – Filter the List of String whose index in second List contains the given Substring
userinput1= input(" Enter your string in the list seperated by a comma:")
strlist1=userinput1.split(',')
print("List of strings is:",strlist1)

userinput2= input(" Enter your substring  in the second list seperated by a comma:")
strlist2=userinput2.split(',')
print("List of strings is:",strlist2)

newlist=[]
for i in range(min(len(strlist1), len(strlist2))):
    if strlist2[i] in strlist1[i]:
        newlist.append(strlist1[i])

print(" Your filered list  based on your substring from your given 2nd list is: ",newlist)        


