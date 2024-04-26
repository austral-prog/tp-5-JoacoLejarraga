def roots(a, b, c):
	x1 = (- b + ( (b *2) - 4 * a * c)*0.5) / (2 * a)
	x2 = (- b - ( (b *2) - 4 * a * c)*0.5) / (2 * a)
	det = (b **2) - 4 * a * c
	if det > 0:
		return f"({x1}, {x2})"
	elif det == 0:
		return f"({x1})"
	else:
		return "( )"
def value_y(a, b, c, x):
	y = (a * (x**2)) + (b * x) + c
	return y
def to_string(a, b, c):
	if a != 0 and b != 0 and c != 0:
		return f"f(x) = {a} * X^2 + {b} * X + {c}"
	elif a == 0 and b != 0 and c != 0:
		return f"f(x) = {b} * X + {c}"
	elif a == 0 and b == 0 and c != 0: 
		return f"f(x) = {c}"
	elif a != 0 and b == 0 and c != 0: 
		return f"f(x) = {a} * X^2 + {c}"
	else:
		return "f(x) = 0"
def derivation(a, b, c):
	if a != 0 and b != 0 and c != 0:
		return f"f'(x) = {2*a} * X + {b}"
	elif a == 0 and b != 0 and c != 0:
		return f"f'(x) = {b}"
	elif a != 0 and b == 0 and c != 0: 
		return f"f'(x) = {2*a} * X"
	else:
		return "f'(x) = 0"
