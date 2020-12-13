#It is just a normal loop function 
# get the user input
n = int(input())
#they want to loop from 1 to 10, in range end is excluded so we use 11 instead of 10
for i in range(1, 11):
	#here we print the output in the form of table.
	print(n, "x", i, "=", n*i)

