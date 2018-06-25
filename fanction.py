def sum (x,y):
	if x > y:
		return y
def sum_two(x,y,z):
	return sum(x, sum_two(y,z))
print(sum_two(3,2,-5))

