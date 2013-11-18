fibnums = [1, 2]

def fib(index):
	if (index < len(fibnums)):
		return fibnums[index]
	else:
		fibnum = fibnums[index - 1] + fibnums[index - 2]
		fibnums.append(fibnum)
		return fibnum

index = 0
fibnum = 0
sum = 0

while fibnum < 4000000:
	fibnum = fib(index)

	if (fibnum % 2 == 0):
		sum += fibnum

	print "index", index
	print "fibnum", fibnum
	print "sum", sum
	print ""

	index += 1