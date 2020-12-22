

n = int(input())
binary = bin(n).replace("0b", "")

print(max(map(len, binary.split("0"))))


