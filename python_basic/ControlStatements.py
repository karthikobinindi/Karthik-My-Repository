
num = 3
if num%2==0:
    print("even")
else:
    print("odd")
marks=100
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
else:
    print("Grade C")

for i in range(1,6):
    print(i)

j = 1
while j<=5:
    print(j)
    j+=1
    if j==2:
        break

# day=2
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thrusday")
add=lambda a,b :a+b
print(add(3,5))

multiplication = lambda c,d:c*d
print(multiplication(3,5))

maxnum = lambda x,y:x if x>y else y
print(maxnum(3,5))

#map(function,iteratble)
numbers=[1,2,3,4,5]
result=map(lambda x:x*2,numbers)
print(list(result))
