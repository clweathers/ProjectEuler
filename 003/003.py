def prime(index):
	previous_prime = prime(index - 1)

	prime = previous_prime + 1

	while (is_prime(prime) == False):
		prime += 1

	return prime

def is_prime(number):
	for divisor in xrange(1, number):
		if (number % divisor == 0):
			return False
	return True

