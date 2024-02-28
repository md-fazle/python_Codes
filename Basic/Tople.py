mytople=("apple","banana","orange")
thistople=("He","Him")
print(mytople)
print(type(mytople))
print(mytople[1])
if "apple" in mytople:
    print("yes")

y=list(mytople)
y.append("mango")
mytople=tuple(y)
print(mytople)

y.remove("apple")
mytople=tuple(y)
print(mytople)

for x in mytople:
    print(x)

for i in range(len(mytople)):
    print(i)

for i in range(len(mytople)):
    print(mytople[i])

thattople=thistople+mytople
print(thattople)

