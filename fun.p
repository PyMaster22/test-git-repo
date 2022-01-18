### Things I think are cool in python 3.8 basically just the walrus operator.
prod=lambda f,l,u:(lambda a,b,c,d:[d:=a(i)*d for i in range(b,c+1)][-1])(f,l,u,1) # Mathematical Product (capital Pi)
fact=lambda x:(lambda y,z:[z:=i for i in range(1,y+1)][-1])(x,1) # Factorial function (!)
# fact=lambda x:prod(lambda y:y,1,x) # Other factorial
summ=lambda f,l,u:sum([f(i) for i in range(l,u+1)]) # Mathematical Summation (capital Sigma)
# summ=lambda f,l,u:(lambda a,b,c,d:[d:=a(i)+d for i in range(b,c+1)][-1])(f,l,u,0) # A more complicated summation. (without sum function)
# and_=lambda x,y:(lambda X:lambda Y:X(Y)(lambda Z:lambda W:W))([lambda X:lambda Y:Y,lambda X:lambda Y:X][x],[lambda X:lambda Y:Y,lambda X:lambda Y:X][y]) # And, but lambda calculus ;) (Doesn't work yet.)
"""
F=lambda x:lambda y:y
T=lambda x:lambda y:x
AND=lambda x:lambda y:x(y)(F)"""
### I don't know what to do now.
