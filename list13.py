#Python | Convert Character Matrix to single String
list1=[]
num= input("Enter your number of rows:")
for i in range(num):
    row=input(f"Enter elements for row{i+1}")
    ele=[e for e in row.split()]
    list1.append(ele)

print(" Your original list is")
for row in list1:
    print(row)

Newlist = ''.join(x for i in list1 for x in i)
print("The String after join : " + Newlist)

