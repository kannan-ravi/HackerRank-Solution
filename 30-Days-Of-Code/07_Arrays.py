size_of_arr = int(input())

arr = input().rstrip().split()
arr_list = list(arr)
arr_list.reverse()
print(" ".join(arr_list))