from sympy import symbols, Wild

# Define your symbols
V, u_x, alpha_x, n, _xi_2, m, p = symbols('V u_x alpha_x n _xi_2 m p')

# Define the pattern with Wild variables
v_w, u_w, alpha_w, n_w, xi_w = symbols('v_w u_w alpha_w n_w xi_w')
pattern = Derivative(xi(v_w, u_w, alpha_w), v_w)*Subs(Derivative(psi(n_w, xi_w), xi_w), xi_w, xi(v_w, u_w, alpha_w))

# Replace the pattern in expr1 with example_expr
result = expr1.replace(pattern, example_expr)

print(result)
