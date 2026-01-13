numbers = [10,20,30,40,50,60]
names = ["Karthik","Vijay","Chiranjeevi","Srikanth"]
mixed = ["karthik",1,True]
print(numbers)
print(names)
print(mixed)
for i in numbers:
    print(i)
if 10 in numbers:
    print("Found")
matrix=[[1,2,3],[4,5,6]]
print(matrix[1][2])
numbers.reverse()
print(numbers)
names.append("Kar")
print(names)
names.extend(["pavan","leela"])
print(names)
names.remove("Kar")
print(names)
names.insert(3,"Sri")
print(names)