import matplotlib.pyplot as plt
import math

plt.figure(figsize = (10, 5))

#f(x) = -5t² - 20t + 15
a = -5
b = -20
c = 15
delta = b * b - 4 * a * c

x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

x_vals = []
y_vals = []

x = 0

while x <= 10:
	y = (-5*x*x) + (20*x) + 15
	y_vals.append(y)
	x_vals.append(x)
	x += 0.1

print("delta:", delta)
print("x1:", x1)
print("x2:", x2)

plt.plot(x_vals, y_vals)

plt.axhline(0, color="orange", linewidth=1)
plt.axvline(0, color="orange", linewidth=1)

plt.title("Gráfico de f(x) = -5x² + 20x + 15")
plt.xlabel("x")
plt.ylabel("y")

plt.grid(True)
plt.show()

#plt.scatter((-1, 3), (0, 0), c = "blue", label = "raizes")
#plt.legend()