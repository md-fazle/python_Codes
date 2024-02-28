myset={"apple","banana","cherry"}
topical={"pineapple","mango"}
myList=["kiwi","this"]
print(myset)
print(len(myset))
print(type(myset))

for i in myset:
    print(i)

myset.add("orange")
print(myset)

myset.update(topical)
myset.update(myList)
myset.remove("this")
print(myset)

x=myset.pop()
print(x)
print(myset)


