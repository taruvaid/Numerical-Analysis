import numpy as np
import matplotlib.pyplot as plt

# Define the functions f1(x) and f2(x)
def f1(x):
    return np.abs(x)

def f2(x):
    return np.sign(x)

# Generate uniform points on the interval [-1, 1]
def uniform_points(n):
    return np.linspace(-1, 1, n)

# Generate Chebyshev points on the interval [-1, 1]
def chebyshev_points(n):
    k_values = np.arange(n)
    return np.cos((2 * k_values + 1) * np.pi / (2 * n))

# Calculate the Lagrange basis polynomial
def lagrange_basis(x, k, points):
    basis = 1.0
    for i in range(len(points)):
        if i != k:
            basis *= (x - points[i]) / (points[k] - points[i])
    return basis

# Perform Lagrange interpolation
def lagrange_interpolation(x, points, func):
    result = 0.0
    for k in range(len(points)):
        result += func(points[k]) * lagrange_basis(x, k, points)
    return result

# Plot the interpolation results for different values of n
def plot_summary(n_values):
    x_vals = np.linspace(-1, 1, 1000)
    plt.figure(figsize=(12, 6))
    
    for n in n_values:
        uniform_pts = uniform_points(n)
        chebyshev_pts = chebyshev_points(n)
        
        # Calculate Lagrange interpolation for f1(x) and f2(x)
        L_uniform_f1 = [lagrange_interpolation(x, uniform_pts, f1) for x in x_vals]
        L_chebyshev_f1 = [lagrange_interpolation(x, chebyshev_pts, f1) for x in x_vals]
        
        L_uniform_f2 = [lagrange_interpolation(x, uniform_pts, f2) for x in x_vals]
        L_chebyshev_f2 = [lagrange_interpolation(x, chebyshev_pts, f2) for x in x_vals]
        
        plt.subplot(2, 2, 1)
        plt.plot(x_vals, f1(x_vals), label=f"f1(x)")
        plt.plot(x_vals, L_uniform_f1, label=f"L{n}(x) (Uniform)")
        plt.title(f"Uniform Points - f1(x) (n={n})")
        plt.legend()
        
        plt.subplot(2, 2, 2)
        plt.plot(x_vals, f1(x_vals), label=f"f1(x)")
        plt.plot(x_vals, L_chebyshev_f1, label=f"L{n}(x) (Chebyshev)")
        plt.title(f"Chebyshev Points - f1(x) (n={n})")
        plt.legend()
        
        plt.subplot(2, 2, 3)
        plt.plot(x_vals, f2(x_vals), label=f"f2(x)")
        plt.plot(x_vals, L_uniform_f2, label=f"L{n}(x) (Uniform)")
        plt.title(f"Uniform Points - f2(x) (n={n})")
        plt.legend()
        
        plt.subplot(2, 2, 4)
        plt.plot(x_vals, f2(x_vals), label=f"f2(x)")
        plt.plot(x_vals, L_chebyshev_f2, label=f"L{n}(x) (Chebyshev)")
        plt.title(f"Chebyshev Points - f2(x) (n={n})")
        plt.legend()
    
    plt.tight_layout()
    plt.show()

# Set the values of n for investigation
n_values = [16]
plot_summary(n_values)
