#Python – Remove words containing list characters
userinput= input(" Enter your string in the list seperated by a comma:")
strlist=userinput.split(',')
print("List of strings is:",strlist)
char=input("Enter your list of chracters:")
char1=char.split(',')
print("List of chrachters is:",char1)
flag=1
new_list=[]
for i in strlist:
    for x in char1:
        if x not in i:
            flag=1
        else:
            flag=0
            break
    if flag==1:
        new_list.append(i)
print("Your modified list after removing list of  starting chracters :",str(new_list))





