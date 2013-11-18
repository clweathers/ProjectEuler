primes = [1,2,3,5,7]

def number_is_prime(number):
	for prime in primes:
		if (prime != 1 and number % prime == 0)
			return False
	return True

def next_prime_after_prime(prime):
	while True:
		prime += 2
		if (number_is_prime(prime)):
			return prime;

def prime_at_index(index):
	if (index < len(primes)):
		return primes(index)
	else
		previous_index = index - 1
		previous_prime = primes[previous_index]
		prime = next_prime_after_prime(previous_prime)
		primes.append(prime)
		return prime

def greatest_prime_factor(number):
	prime_factors = prime_factors(number)
	greatest_prime_factor = prime_factors[-1]
	return greatest_prime_factor

def prime_factors(number):
	for prime in reverse(primes):
		return

for x in xrange(1,600851475143 / 2):
	print x