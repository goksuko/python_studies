import math

class pr0():
	def power(x, y):
		return x**y
	
	def log(x, base):
		return math.log(x, base)
	
def main():
	x = int(input("Enter number x: "))
	y = int(input("Enter number y: "))
	print(f"x**y = ", pr0.power(x, y))
	print(f"log (x) = ", int(pr0.log(x, 2)))

if __name__ == "__main__":
	main()