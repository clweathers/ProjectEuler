def fib(index):
	if (index == 0):
		return 1
	elif (index == 1):
		return 2
	else:
		return fib(index - 1) + fib(index - 2)

index = 0
fibnum = 0
sum = 0

while fibnum < 4000000:
	fibnum = fib(index)

	if (fibnum % 2 == 0):
		sum += fibnum

	index += 1

	print "index", index
	print "fibnum", fibnum
	print "sum", sum
	print ""
