#variables
print("Digite o valor de A: ")
a = int(input())
print("Digite o valor de B: ")
b = int(input())
print("Digite o valor de C: ")
c = int(input())

#formulas
delta = (b ** 2) - 4 * a * c 
x1 = (-b + (delta ** 0.5)) / (2 * a)
x2 = (-b - (delta ** 0.5)) / (2 * a)

#set: create a colletion of unordered and unique elements
C = set()

#x receives the value of x1 and x2, not in range bc it asks for an integer value
for x in (x1, x2):
	if x > 0 and x.is_integer():
		C.add(x)

print("Conjunto C =", C)