#Python – Swap elements in String list
userinput= input(" Enter your string in the list")
strlist=userinput.split(',')
print("List of strings is:",strlist)
if len(strlist) < 2:
    print("The list must contain at least two elements to swap.")
else:
    index1 = int(input("Enter the index of the first element to swap: "))
    index2 = int(input("Enter the index of the second element to swap: "))

    if 0 <= index1 < len(strlist) and 0 <= index2 < len(strlist):
        strlist[index1], strlist[index2] = strlist[index2], strlist[index1]
        print("List after swapping elements in a string :")
        print(strlist)
    else:
        print("Invalid index values. Please enter valid indices within the range of the list.")







