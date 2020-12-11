def main(f):
	n = []
	f = open(f, "r")
	for line in f:
		n.append(int(line))
	
	# Find the two entries that sum to 2020; what do you get if you multiply them together ?
	A = 0
	B = 0
	while True:
		B +=1
		if B == len(n):
			A += 1
			B = A+1
		if n[A] + n[B] == 2020:
			print(n[A]*n[B])
			break
	# what is the product of the three entries that sum to 2020?
	A = 0
	B = 1
	C = 2
	while True:
		if n[A] + n[B] + n[C] == 2020:
			print(n[A]*n[B]*n[C])
			break
		C += 1
		if C == len(n):
			B += 1
			C = B+1
		if B == len(n)-1:
			A += 1
			B = A+1
			C = B+1


if __name__ == '__main__':
	main('input1.txt')