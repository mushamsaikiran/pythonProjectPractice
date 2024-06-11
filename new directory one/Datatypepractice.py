"""
num1 = input("Enter the first number:")
num2 = input ("Enter the second number :")
result = type(num1 + num2)
result = int(num1)+ int(num2)
print(result)


# when you want to concentrate string ( combine two strg + strg)

strone  = input("Enter your first name ")
strtwo = input("Enter the last name ")
resultone  = str(strone) + str(strtwo)
print(resultone)
"""

#when you divided by / some value the python will take by default 2.34 ( float)

ravi = 12
ravi2 = 10
resultone = ravi/ravi2
print(resultone)
print(type(resultone))

# The string = string is a bunch of charcter and str indicates '' and "" and """  string

a = 'my  name is sampath and he is working in infosys'
print(a)

b = "He has a good intelligance and he will talk only the priority talks only "
print(b)

c = """ when we use the  thriple cout and we are  going to tirupathi  and is going there and 
he was a good at singing"""
print(c)

# raw string ; r'C:/drive/guys' directery path of the string

# first name and last name formatting the values f indicates

myfirstname = "Harry"
lastname = "potter"
print((f"The f indicates the formatting {myfirstname} {lastname}"))
print(f"{myfirstname} + {lastname}")
print(myfirstname + "" + lastname)
print(myfirstname + lastname)

# Function and strings methods
# what is function : function ia an repeat a task and we can reuse them and these are the strimgs functions


# here are the some String functions  used in python modt important we used
nameone = "Stand your own foot and treated trouble as blessing "

# Print one striing functon
print(nameone)
print(type(nameone))  #-> it say the which datatype it is
print(id(nameone))    # This function say that  memory allocate
print(len(nameone))  #  The length of the string ( it start with the count of 1 )
a = nameone.count("o")
print(a)

# The print value as val
valuee = None
print(valuee)
print(type(valuee))

# List = List is store the multiples items as same as array and it should indicate with the []
shopinglist = ["milk","butter","bread","Sweets","Soaps"]
print(shopinglist)
print(len(shopinglist))
print(shopinglist[3])
print(shopinglist[-2])
print(shopinglist.insert(2,"turmeric"))
print(shopinglist)
print(shopinglist.insert(3,"Chilly powder"))
print(shopinglist)
print(shopinglist.extend(["ginger","sugar","salt"]))
print("&&&&&&&&&&&&&")
print(shopinglist)
print(shopinglist)

print("((((((((((((((((((((((())))))))))")

# The escape sequence by pramod
print("hello\nworld")  # \n it will print the new line in the string
print("Hello\tworld ")  # The new tab space is considered
print("Hello \bworldd")  # Removes the  one inbackspace from the string value "Hello \b"


# crud c for create , r means read and u means update and d fro delete operations


mylistss = ["manual","Api Testing","Database testing","Automation testing"]
print(mylistss)
mylistss.remove("Automation testing")
print(mylistss)
print("@@@@@@@@@@")

print(mylistss)


print("%%%%%%%%%%%")

myworkingss = ["API Testing real","Database testing","python +selenium ","Jenkins"]
print(myworkingss)
myworkingss.pop()
print(myworkingss)

# reverse the strings
myworkingss.reverse()
print(myworkingss)
# Pop is used to remove the last
myworkingss.sort()
print(myworkingss)

# change the index values
myworkingss[1] = " My sql DB "
print(myworkingss)

