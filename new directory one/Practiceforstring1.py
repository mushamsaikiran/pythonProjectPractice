# for  loop is used  to iterating over a sequence  and iterating the loop for over a sequence

thislist = ["Apple","Ball","camel","Dog","Eagle"]
for x in thislist:
    print(x)

print("@@@@@@@@@@@@@@@@")

# for looping concept is iterating over a  sequence ( list,Tuple,string,Dict, set )

list2 = ["Ravi","shiva","madhu","Sampath"]
for y in list2:
    print(y)


list2 = ["karan","laxmi","narayan","naveen"]
for z in  list2:
    print(z)

# Looping through a string ( Even string are iterable objects, they contain a sequence of charcters )

for x in "banana":
    print(x)

for q  in "Queen":
    print(q)


# In for loop  we can break the loop interating by using the break command;

mylist = ["Tata","Biral","ratan","soft"]
for x in mylist:
    print(x)
    if  x == "ratan":
        break

myname = ["ravi","shiva","hari","ganesh"]
for ya in myname:
    print(ya)
    if ya == "ganesh":
       break

# for loop in string iteration over a sequence

for xc in "Musham":
    print(xc)


fruits = ["apple","mango","cherry","curry"]
newlistt = []

for x in fruits:
    if  "a" in x:
        newlistt.append(x)
print(newlistt)


# In the python list > The Sort method ; Sort method always start with the asceding order

listone = ["apple","orange","Mango","Pineapple","Bat","elephant"]
listone.sort()
print(listone)

numberslist = [2,10,4,9,6,1]
numberslist.sort()
print(numberslist)

# The alphabets ascending order
thislistone = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislistone.sort()
print(thislistone)

# The descending order to acending order
thisdes = [20,60,100,10,5,18,78]
thisdes.sort()
print(thisdes)
#
thisdes.sort(reverse=True)
print(thisdes)

# IN THE LIST THE REVERSE ORDER IS USED

reverseord = ["Apple","Orange","Mango","Banana","zoo"]
reverseord.reverse()
print(reverseord) # the output was  rzoo ,banana, mango,orange,apple

# in the list reverse the number in list
numtwo = [2, 10, 50, 100, 150 , 200 ,5]
numtwo.reverse()
print(numtwo)

hello1 = ["Hello","World"]
hello1.reverse()
print(hello1)  # hello  - > olleh it only reverse the order of the items not  the string


# The list > the copied methods

print("%%%%%%%%%%%%%%%%%")
hello1 = ["Hello","World"]
hello1.copy()
print(hello1)

# Join method in the list () ; joining the two list in the string

list1 = ["abc","def","ghi","jkl","mno"]
list2 = [1,2,3,4,5,6]
list3 = list1 + list2
print(list3)

#







