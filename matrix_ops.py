class Value:
    def __init__(self, data, _children=()):
        self.data( = data
        self._prev = set(_children) #trackes nodes that created this value

    def __repr__(self):
	return f"Value(data={self.data})"

    def __add__(self, other):
	# to write a + b
	out = Value(self.data + other.data(self, other))
	return out
	# to write a * b
    def __mul__(self, other):
	out = Value(self.data * other.data(self, other))
	return out

#testing 

a = Value(2.0)
b = Value(3.0)
c = a + b
d = a * b
print(f"Addition result: {c}")
print(f"Multiplication result: {d}")
