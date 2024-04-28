
#pip install scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Define the function f(t)
def f(t):
    return 1 / (1 + 6 * t**2)

# Lagrange polynomial interpolation at uniform points
def lagrange_uniform(x, y, t):
    n = len(x)
    L = np.zeros_like(t)
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (t - x[j]) / (x[i] - x[j])
        L += term
    return L

# Lagrange polynomial interpolation at Chebyshev points
def lagrange_chebyshev(n, t):
    x_chebyshev = np.cos((2 * np.arange(1, n + 1) - 1) * np.pi / (2 * n))
    y_chebyshev = f(x_chebyshev)
    return lagrange_uniform(x_chebyshev, y_chebyshev, t)

# Generate points for plotting
t_values = np.linspace(-1, 1, 1000)
f_values = f(t_values)

# Interpolate at different values of n
n_values = [5, 10, 20]
plt.figure(figsize=(10, 6))
for n in n_values:
    plt.plot(t_values, lagrange_chebyshev(n, t_values), label=f"Lagrange (Chebyshev) n={n}")

plt.plot(t_values, f_values, label="f(t)", color='blue', linewidth=2)
plt.xlabel("t")
plt.ylabel("f(t) / L_n(t)")
plt.title("Lagrange Polynomial Interpolation")
plt.legend()
plt.grid(True)
plt.show()


# Generate n uniform points in the interval [-1, 1]
def generate_uniform_points(n):
    return np.linspace(-1, 1, n)

# Compute natural cubic spline interpolation
def natural_cubic_spline(x, y, t):
    cs = CubicSpline(x, y, bc_type='natural')
    return cs(t)

# Generate points for plotting
t_values = np.linspace(-1, 1, 1000)
f_values = f(t_values)

# Interpolate at different values of n
n_values = [8, 16, 32]
plt.figure(figsize=(10, 6))
for n in n_values:
    x_uniform = generate_uniform_points(n)
    y_uniform = f(x_uniform)
    plt.plot(t_values, natural_cubic_spline(x_uniform, y_uniform, t_values), label=f"Spline n={n}")

plt.plot(t_values, f_values, label="f(t)", color='green', linewidth=2)
plt.xlabel("t")
plt.ylabel("f(t) / S_n(t)")
plt.title("Natural Cubic Spline Interpolation")
plt.legend()
plt.grid(True)
plt.show()


x_lagrange = generate_uniform_points(8)
y_lagrange = f(x_lagrange)
plt.plot(t_values, lagrange_uniform(x_lagrange, y_lagrange, t_values), label="Lagrange n=32", color='orange')
plt.plot(t_values, f_values, label="f(t)", color='blue', linewidth=4)

n_values = [8]
for n in n_values:
    x_uniform = generate_uniform_points(n)
    y_uniform = f(x_uniform)
    plt.plot(t_values, natural_cubic_spline(x_uniform, y_uniform, t_values),color='red',linewidth=2, label=f"Spline n={n}")


plt.xlabel("t")
plt.ylabel("f(t) / Interpolations")
plt.title("Lagrange vs. Natural Cubic Spline Interpolation")
plt.legend()
plt.grid(True)
plt.show()
