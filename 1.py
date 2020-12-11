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
			B = A + 1
		if n[A] + n[B] == 2020:
			print(n[A]*n[B])
			break

if __name__ == '__main__':
	main('input.txt')