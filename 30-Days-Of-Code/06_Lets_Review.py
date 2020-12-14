
T = int(input())
for S in range(T):
	S = input()
	even = ""
	odd = ""
	for i, string in enumerate(S):
		if (i % 2) == 0:
			even = even + string
		else:
			odd =  odd + string
	print(even, odd)
