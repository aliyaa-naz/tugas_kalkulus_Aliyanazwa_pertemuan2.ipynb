# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 5, 400)
y = 3 * x - 6

plt.figure(figsize=(7, 5))
plt.plot(x, y, label="$f(x) = 3x - 6$", color="blue", linewidth=2)

# Titik Potong
plt.scatter([2, 0], [0, -6], color="red", zorder=5)
plt.annotate(
    "Potong Sumbu-X (2, 0)",
    (2, 0),
    textcoords="offset points",
    xytext=(10, -10),
)
plt.annotate(
    "Potong Sumbu-Y (0, -6)",
    (0, -6),
    textcoords="offset points",
    xytext=(10, 0),
)

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.title("Soal 1: $f(x) = 3x - 6$")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.show()


