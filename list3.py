#Python program to find the character position of Kth word from a list of strings
userinput= input(" Enter your string in the list seperated by a comma:")
strlist=userinput.split(',')
print("List of strings is:",strlist)
k=20
indexcounter=0
for i in strlist:
    if (indexcounter +len(i)) > k:
        print("Index at the kth position is :",str(k-indexcounter))
        break
    else:
        indexcounter=indexcounter+len(i)
else:
    print("k th position is beyound position of the list")        

