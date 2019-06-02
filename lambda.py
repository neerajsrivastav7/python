f=lambda x,y,z:x+y+z
print(f(3,4,5))


L = [(lambda x: x**2), (lambda x: x**3), (lambda x: x**4)] #we can put lambda as list object
for f in L:
  print(f(2))
print(L[0](3))

value=lambda x:(1 if x>0 else 0)
print(value(9))
print(value(-9))


def action(y):
  return (lambda x:x+y)
act=action(99)
print(act)# act have the lambda (lambda x:x+99) this is the lambda object send by action  
print(act(2)) # here the result will be 101


action=(lambda x: (lambda y:x+y))# we can acheive the above action by lambda
act=action(99)
print(act(5))

print((lambda x: (lambda y:x+y))(99)(10))  #directly we can use the lambda to call the above function


# apply build in function in python3

#f=lambda x,y,z:x+y+z
#print(apply(f,(2,3,4))) apply is not define in python3




