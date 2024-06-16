def findTrailingZeros(n):
	count = 0
	i = 5
	while (n / i>= 1):
		count += int(n / i)
		i *= 5

	return int(count)

# Driver program
n = 100
print("Count of trailing 0s "+
	"in 100 ! is", findTrailingZeros(n))