#Python – Add Space between Potential Words
userinput = input("Enter your string:").split(',')  
print("List of strings is:",userinput)
newlist=[]
for i in userinput:
    for j in i:
        if(j.isupper()):
            i=j.replace(j,' '+ j )
    newlist.append(i)
print("Your modified list based on upper case is :", newlist)            