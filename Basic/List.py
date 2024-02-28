A=["A","B","C","D","E","F","G"]
B=["T","O","P"]
print(A)
print(len(A))
print(A[-1])
print(A[2:5])

if "C" in A:
    print("yes")

A.append("H")
print(A)    

A.extend(B)
print(A)

for x in A:
    print(x)