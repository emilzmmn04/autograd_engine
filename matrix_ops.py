class Value:
    def __init__(self, data, _children=()):
        self.data = data
        self.grad = 0.0      #Gradient
        self._prev = set(_children) #trackes nodes that created this value

    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other):
	# to write a + b
        out = Value(self.data + other.data, (self, other))        
        def _backward():
            self.grad += 1.0 * out.grad
            other.grad += 1.0 * out.grad
        out._backward =  _backward
        return out
	
    def __mul__(self, other):
	# to write a*b
        out = Value(self.data * other.data, (self, other))
        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward =  _backward
        return out

    def __sub__(self, other):
	# to write a - b 
        out = Value(self.data - other.data, (self, other))
        def _backward():
            self.grad += 1.0 * out.grad
            other.grad += -1.0 * out.grad
        out._backward =  _backward
        return out

    def backward(self):
        topo = []
        visited = set()
        def build_topo(v):
             if v not in visited:
               visited.add(v)
               for child in v._prev:
                   build_topo(child)
               topo.append(v)

        build_topo(self)

        self.grad = 1.0

        for node in reversed(topo):
            if hasattr(node, '_backward'):
                 node._backward()

     
    def relu(self):
        out = Value(max(0.0, self.data), (self,))

        def _backward():

            self.grad += (1.0 if self.data > 0 else 0.0) * out.grad

        out._backward = _backward

        return out

    def zero_grad(self):
        self.grad = 0.0



    def zero_grad(self):
        self.grad = 0.0



# --- Testing ---
a = Value(2.0)
b = Value(3.0)
c = a + b 
d = a * b 

# 1. Test c.backward()
c.backward()
print(f"a.grad after c: {a.grad}") # Expect 1.0
print(f"b.grad after c: {b.grad}") # Expect 1.0

# 2. RESET before the next pass!
a.grad = 0.0
b.grad = 0.0
c.grad = 0.0
d.grad = 0.0

# 3. Test d.backward()
d.backward()
print(f"a.grad after d: {a.grad}") # Expect 3.0
print(f"b.grad after d: {b.grad}") # Expect 2.0
