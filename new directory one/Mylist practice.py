# Advance datatype in python  are list,tuple,set,dict

myList = ["UI test", "performance", "Security test"]
print(myList)

# add the values into list of variable

print(myList.append("Automation test"))

# adding the values in the list (multiple records list in array)
# print(myList.insert("Compatablity test"))

mylist = ["apple", "banana", "cherry"]
print(mylist)

Thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(Thislist)
print(len(Thislist))  # the length will start from 1  , 1 count

list1 = ["apple", "banana", "cherry"]
print(list1)
list2 = [1, 5, 7, 9, 3]
print(list2)
list3 = [True, False, False]
print(list3)

list4 = ["apple", 45, True, 56, "Orange"]
print(list4)

print("#################")

thislist5 = list(("ravi", "shiva", "ganesh", "Hari"))  # note the double round-brackets
print(thislist5)
thislist5[0] = "Sai kiran"
print(thislist5)
print(thislist5[3])  # hari

# In a list the Postive  index will start from begging of list (0,1,2)
myarr = "unit", "Integration", "System", "Acceptance"
print(myarr[2])

# IN a list the negative index will start from ending of the string count will start ;

myskills = ["manual testing", "API testing", "Automation testing"]
print(myskills)
print(myskills[-2])  # print the api testing

# The range of indexes in the list ( We know that start from the index and ending at the index )
thislistawe = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislistawe[1])
print(thislistawe[2:5])  # print (cherry , orange, kiwi , melon )

# print(list3.append("test"))

print("########Testing is craft and asking question,understanding the product and Different perspective to test")

negativeindex = ["confidence","skills","Learning","Practice and implement"]
print(negativeindex[-1])
print(negativeindex[-2])
print(negativeindex[2:4])
print(negativeindex[-1:-3])


thislistrav = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] # 2,3,4 ( orange,kiwi,melon)
print(thislistrav[2:5])
# leaving the starting value range

print("%%%%%%%%%%%%%%%%%%%%")
thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist3[:4])

thislist5 =  ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist5[3:]) # orange,kiwi ,melon , mango

