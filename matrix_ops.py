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

