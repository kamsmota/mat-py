import matplotlib.pyplot as plt

plt.figure(figsize = (10, 5))

x_vals = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
y_vals = [21, 12, 5, 0, -3, -4, -3, 0, 5]

#x²

plt.plot(x_vals, y_vals, label = "f(x) = x² - 2x - 3", color = "purple")

plt.axhline(12, color = "orange", linewidth = 1)
plt.axvline(1, color = "orange", linewidth = 1)
plt.scatter((-1, 3), (0, 0), c = "blue", label = "raizes")

plt.title("gráfico de x com y")
plt.ylabel("eixo de y")
plt.xlabel("eixo de x")

plt.grid(True)
plt.legend()
plt.show()