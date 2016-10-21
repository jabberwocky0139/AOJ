# coding: utf-8

f = open("input.txt")
iterator = (("NS", "S"), ("NT", "T"))
var = {}

for i, j in iterator:
    var[i] = int(f.readline())
    var[j] = [int(k) for k in f.readline().split()]

count = 0
for T in var["T"]:
    left = 0
    right = len(var["S"])
    while(left < right):
        mid = (left + right)//2
        if var["S"][mid] == T:
            count += 1
            break
        elif var["S"][mid] <= T:
            left = mid+1
        else:
            right = mid
print(count)
