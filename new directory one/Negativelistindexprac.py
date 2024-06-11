
# negative index in list, it will count the string from the ending of the string
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])  # the output  melon, kiwi, orange   ( reverse  negative index first -1 won't count in the string
#

#Practice more examples range of indexes in list (postive index and negative index)

"""
for the postive index  starting from the starting of the string 
 3 : 5  -> 5 index is not count ( before 5 index only the values it return)
 
 ----------------
 
 for 2 : 8 
 
 the 8 index should not considered, only up to  7 index should return 
"""



mynames = ["apples","Boy","cat","Dog","eagle","fish","goat"]
#            0      , 1,   2   , 3   , 4     , 5     , 6
print(mynames[2:5]) # cat,dog,eagle  ( for postive index starting range value count 2 : (5) for ending of the range it wont count index


myindexnegative = ["apples","Boy","cat","Dog","eagle","fish","goat"]
#             #    {   -7    } { -6 }, { -5  },{-4}  , {-3  }  ,  {  -2} , { -1  }
print(myindexnegative[-4:-1]) # dog, eagle , fish

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
"""
for the negative index values -4 : -1  -> the last values  means -1 It won't considered 

for the negative index values -8 : -6  -> for last values of index means -6 it won't consider )return upto -5 in string )

example postive index range 4 : 7 

alpha = ["aeroplane","bat","car","drive","ear","flag","Horse","ink","jeep","king"]
print(alpha[4:7])  #  ear,flag,horse 

print(alpha[-4:-3]) # "drive","ear","flag","Horse","ink","jeep","king




"""
alpha = ["aeroplane","bat","car","drive","ear","flag","Horse","ink","jeep","king"]
print(alpha[4:7])  #  ear,flag,horse

print(alpha[-2:-5])

print(alpha[-3:-1]) # "drive","ear",
print(alpha[-4:-3])# "flag


# ","Horse","ink","jeep","king

# In operator in the python , In string the words are present in array list or not

thislist = ["apple", "banana", "cherry"]
if "appleee" in thislist:
  print("Yes, 'apple' is in the fruits list")

else:
     print("No value")


namess = ["ganesh","Hari","Ravi","Shiva"]
if "Hariii" in namess:
    print("True sucess")
else :
    print("no name")


name = ["testing","manual testing ","API Testing","Automation","performance"]
if "API Testing" in name:
    print("Success grand 200")
else:
    print("Error message is displayed 500")


test1 = ["Testing","API testing","Manual testing"]
test2 = ["Integration","System testing","functional testing"]
test1.extend(test2)
print(test1)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple","test","saikumar"]
thislist.pop(2)
print(thislist)

thislist = ["apple","test","saikumar"]
thislist.pop(0)
print(thislist)


thislist = ["Saikiran","Ravi","Saikumar","testing"]
thislist.pop()
print(thislist)


thislist = ["saikiran","ravi","sai","saikumar"]
del thislist[1]
print(thislist)


# Delete the entire  content from the list
thislist = ["saikiran","ravi","sai","saikumar"]
del thislist
print(thislist) # The output is shows the error because delete the total list of iteams

# The clear method in string ; it remove all the content in the list

thislist = ["joshuva","Sravya","nitish"]
thislist.clear()
print(thislist)  # the list inside the content was cleared and return the empty string


