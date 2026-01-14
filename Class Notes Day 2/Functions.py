def add(a,b):
    print(a+b)
add(10,20)

def sub(c,d):
    return c-d,c
print(sub(20,10))

def hello(name):
    print(name)
hello("hi Karthik")

def hello(greeting="Hello",name="world"):
    print('%s,%s'%(greeting,name))
hello()
hello('greetings','Karthik')
def print_params(*params):
    print(params)
print_params('Testing')
print_params(1,2,3,4,)

def print_params(**params):
    print(params)

print_params(x=1,y=2,z=3)
