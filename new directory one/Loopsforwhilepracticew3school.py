"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#print("breakone")

fruits = ["apple", "banana", "cherry"]
for c in fruits:
    print(c)
    if c == "banana":
        break
    print(c)
"""

#print("break two ")
fruits = ["apple", "banana", "cherry"]
for t in fruits:
    if t == "banana":
        continue
    print(t)

print("Divideding ")

# Break ( break should be stop the loop even the condition is true
names = ["saikiran","musham","netha","testing","naren","laddu","pinky","hari"]
for r in names:
    print(r)
    if r == "laddu":
        break

# Continue : for the specifiuc condition iteration is stop or skipped and moved to the next iteration
myskilsset = ["manual","Api tetsing","Automation testing","communication","logical thinking"]
for m in myskilsset:
    if m =="Automation testing":
       continue
    print(m)
