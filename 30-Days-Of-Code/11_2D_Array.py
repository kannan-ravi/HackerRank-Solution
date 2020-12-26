'''
There are 6 lines of input, where each line contains 6 space-separated integers that describe the 2D Array A

Print the maximum hourglass sum A

[[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]

1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6

 a b c
   d
 e f g
'''

def sumthe_matrix(matrix, i, j):
	a = matrix[i-1][j-1]
	#print(a)
	b = matrix[i-1][j]
	#print(b)
	c = matrix[i-1][j+1]
	#print(c)
	d = matrix[i][j]
	#print(d)
	e = matrix[i+1][j-1]
	#print (e)
	f = matrix[i+1][j]
	#print(f)
	g = matrix[i+1][j+1]
	#print(g)
	
	return (a + b + c + d + e + f + g)

arr = []
result = []
for _ in range(6):
	arr.append(list(map(int, input().split(" "))))
	
'''
arr = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
'''


for row in range(1,5):
	for column in range(1,5):
		adding = sumthe_matrix(arr , row , column)
		result.append(adding)
		
print(max(result))