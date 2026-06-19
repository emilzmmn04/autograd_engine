from matrix_ops import Value

# --- Testing the Engine ---

# 1. Test c.backward()
a = Value(2.0)
b = Value(3.0)
c = a + b
c.backward()

print(f"a.grad after c: {a.grad}") # Expect 1.0
print(f"b.grad after c: {b.grad}") # Expect 1.0

# 2. RESET before the next pass
a.grad = 0.0
b.grad = 0.0

# 3. Test d.backward()
d = a * b
d.backward()

print(f"a.grad after d: {a.grad}") # Expect 3.0
print(f"b.grad after d: {b.grad}") # Expect 2.0

# 4. Test ReLU
x = Value(-2.0)
y = x.relu()
y.backward()
print(f"x.grad after relu: {x.grad}") # Expect 0.0
