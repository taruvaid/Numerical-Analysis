import numpy as np
import matplotlib.pyplot as plt

# function f(t)
def f(t):
    return 1 / (t + 1)

#Bernstein polynomial function
def bernstein_polynomial(t, n, f):
    result = 0
    for i in range(n+1):
        result += f(i/n) * np.math.comb(n, i) * (t ** i) * ((1 - t) ** (n - i))
    return result

# Generate points for plotting
t_values = np.linspace(0, 1, 1000)
f_values = f(t_values)

# Plot the function f(t)
plt.figure(figsize=(10, 6))
plt.plot(t_values, f_values, label='$f(t) = \\frac{1}{t + 1}$', color='blue')

# Plot the Bernstein polynomials for n = 1, 2, 4, 8, 16, 32
n_values = [1, 2, 4, 8, 16, 32]
colors = ['red', 'green', 'orange', 'purple', 'brown', 'magenta']
for i, n in enumerate(n_values):
    bernstein_values = [bernstein_polynomial(t, n, f) for t in t_values]
    plt.plot(t_values, bernstein_values, label=f'$B_{n}(t; f)$', color=colors[i], linestyle='--')

plt.title('Bernstein Polynomials vs. $t$')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

#error estimation function
def error_estimate(n, f):
    t_values = np.linspace(0, 1, 1000)
    f_values = f(t_values)
    bernstein_values = np.array([bernstein_polynomial(t, n, f) for t in t_values])
    return np.max(np.abs(f_values - bernstein_values))

# Compute the error estimate forn_values = [1, 2, 4, 8, 16, 32]
n = 1
error = error_estimate(n, f)
print(f"Error estimate for n = {n}: {error}\n")

n = 2
error = error_estimate(n, f)
print(f"Error estimate for n = {n}: {error}\n")

n = 4
error = error_estimate(n, f)
print(f"Error estimate for n = {n}: {error}\n")

n = 8
error = error_estimate(n, f)
print(f"Error estimate for n = {n}: {error}\n")

n = 16
error = error_estimate(n, f)
print(f"Error estimate for n = {n}: {error}\n")

n = 32
error = error_estimate(n, f)
print(f"Error estimate for n = {n}: {error}\n")
