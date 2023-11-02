#Python – Prefix frequency in string List
userinput= input(" Enter your string in the list seperated by a comma:")
strlist=userinput.split(',')
print("List of strings is:",strlist)
s1=input("Enter the string you want to check its frequency:")
count =0
for i in strlist:
    if i.startswith(s1):
       count=count+1
print(" Your frequency of the entered substring is:",count)    