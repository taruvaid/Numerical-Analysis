
#cosine

import numpy as np
import matplotlib.pyplot as plt

def chebyshev_T(n, x):
    return np.cos(n * np.arccos(x))

x_vals = np.linspace(-1, 1, 1000)
plt.figure(figsize=(8, 6))

for n in range(5):
    plt.plot(x_vals, chebyshev_T(n, x_vals), label=f"T_{n}(x)")

plt.title("Chebyshev Polynomials of the First Kind")
plt.xlabel("x")
plt.ylabel("T_n(x)")
plt.legend()
plt.grid(True)
plt.show()

#sine
def chebyshev_U(n, x):
    return np.sin((n + 1) * np.arccos(x)) / np.sqrt(1 - x**2)

plt.figure(figsize=(8, 6))

for n in range(5):
    plt.plot(x_vals, chebyshev_U(n, x_vals), label=f"U_{n}(x)")

plt.title("Chebyshev Polynomials of the Second Kind")
plt.xlabel("x")
plt.ylabel("U_n(x)")
plt.legend()
plt.grid(True)
plt.show()
