import sys
n = int(input())

dock = {}
for i in range(n):
	dictionary = input().split()
	doc = {dictionary[0] : dictionary[1]}
	dock.update(doc)

whole = sys.stdin.readlines()
for i in whole:
	user = i.strip()
	if user in dock:
		print(f"{user}={str(dock[user])}")
	else:
		print("Not found")
	