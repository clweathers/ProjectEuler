def reversed_string(string):
	reversed_string = string[::-1]
	return reversed_string

def is_palindrome(number):
	number_string = str(number)
	reversed_number_string = reversed_string(number_string)
	is_palindrome = (number_string == reversed_number_string)
	return is_palindrome

def largest_number_with_digits(digits):
	nines = ["9" for x in range(digits)]
	largest_number_string = "".join(nines)
	largest_number = int(largest_number_string)
	return largest_number

def smallest_number_with_digits(digits):
	digits = ["0" for x in range(digits - 1)]
	digits.insert(0, "1")
	smallest_number_string = "".join(digits)
	smallest_number = int(smallest_number_string)
	return smallest_number

def palindromes_with_digits(digits):
	palindromes = []
	largest_number = largest_number_with_digits(digits)
	smallest_number = smallest_number_with_digits(digits)
	for x in xrange(largest_number,smallest_number,-1):
		for y in xrange(largest_number,smallest_number,-1):
			product = x * y
			product_is_palindrome = is_palindrome(product)
			if (product_is_palindrome):
				palindromes.append(product)
	return palindromes

def largest_palindrome_with_digits(digits):
	palindromes = palindromes_with_digits(digits)
	largest_palindrome = max(palindromes)
	return largest_palindrome

largest_palindrome = largest_palindrome_with_digits(3)
print largest_palindrome