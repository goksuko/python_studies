#proportonal 
# number of operations is directly proportional to the size of the input
# O(n)
# y = x graph

def sum1(n):
	final_sum = 0
	for i in range(n):
		final_sum += i
	return final_sum

sum1(10)

def print_items(n):
	for i in range(n):
		print(i)

print("print_items")
print_items(10)

# Drop Constants => First rule of simplifying Big O notation
# O(n + n) => O(2n)
# O(2n) => O(n)

def print_items_2(n):
	for i in range(n):
		print(i)

	for j in range(n):
		print(j)

print("print_items_2")
print_items_2(10)

# O(n * n) => O(n^2)
# y = x^2 graph

def print_items_3(n):
	for i in range(n):
		for j in range(n):
			print(i, j)

print("print_items_3")
print_items_3(10)

# Drop Non Dominants => Second rule of simplifying Big O notation
# O(n + n^2) => O(n^2)

def print_items_4(n):
	for i in range(n):
		print(i)

	for i in range(n):
		for j in range(n):
			print(i, j)

print("print_items_4")
print_items_4(10)

# divide and conquer
# O(log n)
# y = log(x) graph

def divide_by_2(n):
	while n > 0:
		n = n // 2
		print(n)

print("divide_by_2")
divide_by_2(8)

# O(1)
# y = 1 graph

def func_constant(values):
	print(values[0])

print("func_constant")
func_constant([1, 2, 3])

# Different terms for inputs
# if the function has two inputs, n and m
# you can't add them
# you can't multiply them
# O(n + n) => O(2n) => O(n)
# O(n + m)
# O(n * n) => O(n^2)
# O(n * m)

def func_lin_m(n, m):
	for i in range(n):
		print(i)

	for i in range(m):
		print(i)

# big O for lists
# O(n) for append
# O(n) for pop
# O(n) for pop(i)
# O(n) for insertion
# O(n) for deletion

# O(1) for last element
# O(1) for indexing

#################################
# O(n^2) Loop within a loop
# O(n) Proportional
# O(log n) Divide and conquer
# O(1) Constant

# O(1) — Constant Time: The algorithm’s running time does not depend on the size of the input; it performs a fixed number of operations.
# O(log n) — Logarithmic Time: The algorithm’s running time grows logarithmically with the size of the input.
# O(n) — Linear Time: The algorithm’s running time scales linearly with the size of the input.
# O(n log n) — Linearithmic Time: The algorithm’s running time grows in proportion to n times the logarithm of n.
# O(n²) — Quadratic Time: The algorithm’s running time is directly proportional to the square of the input size.
# O(2^n) — Exponential Time: The algorithm’s running time doubles with each increase in the input size.
# O(n!) — Factorial Time: The algorithm’s running time is a multiple of the factorial of the input size.



#https://www.bigocheatsheet.com/