# Operadores de identidade são: 'is' e 'is not'.


saldo = 1000
limite = 1000

print(saldo is limite)
print(saldo is not limite)

print()

a = [1, 2, 3]  
b = a  
print(a is b) # True

a = [1, 2, 3]  
b = [1, 2, 3]  
print(a is b)

x = 100  
y = 100  
print(x is y) 

x = 257  
y = 257
print(x is y)  

x = 257  
y = [257]
print(x is y) 

a = "Python"  
b = "Python"  
print(a is b)

a = [4, 5, 6]  
b = [4, 5, 6]  
print(a is not b)

x = None  
y = None  
print(x is y) 

a = True  
b = 1  
print(a is b)
