def setbit_down(A, x, n) :
	if x >= n :
		return
	if 2 * x + 1 <= n and A[2 * x + 1] == 0 :
		A[2 * x + 1] = 1
		setbit_down(A, 2 * x + 1, n)
	if 2 * x + 2 <= n and A[2 * x + 2] == 0 :
		A[2 * x + 2] = 1
		setbit_down(A, 2 * x + 2, n)


def set_bit(A, pos, length) :
	if not A or pos<0 or length <= 0 :
		return
	n = len(A) - 1    #last index of A
	for x in range(pos, min(n + 1, min(pos + length, 2 * pos + 1))) :
		# set self
		if A[x] == 1:
			continue
		A[x] = 1
		# set descendants
		setbit_down(A, x, n)
		# set ancestors
		while x>0:
			if (x % 2 == 0 and A[x - 1] == 1) or (x % 2 == 1 and x<n and A[x + 1] == 1) :
				A[int((x - 1) / 2)] = 1
			x = (x - 1) / 2

def clear_bit(A, pos, length) :
	if not A or pos<0 or length <= 0 :
		return
	n = len(A) - 1    #last index of A
	for x in range(pos, min(n + 1, pos + length)) :
		# clear self
		if A[x] == 0:
			continue
		A[x] = 0
		# clear descendants
		while 2 * x + 1 <= n:
			A[2 * x + 1] = 0
			x = 2 * x + 1
		# clear ancestors
		while x>0:
			if A[int((x - 1) / 2)] == 0 :
				break
			A[int((x - 1) / 2)] = 0
			x = (x - 1) / 2

if __name__ == '__main__' :
	A = [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
	test_cases = [(x, y) for x in range(len(A)) for y in range(1, len(A) - x + 1)]

for each_test_case in test_cases:
	pos, length = each_test_case
	A = [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
	set_bit(A, pos, length)
	print(f'after setting bit from {str(pos)} for {str(length)} A is: {A}')
	A = [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
	clear_bit(A, pos, length)
	print(f'after clearing bit from {str(pos)} for {str(length)} A is: {A}')