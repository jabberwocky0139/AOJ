# coding: utf-8
from collections import deque

f = open("input.txt")
iterator = [["NS", "S"], ["NT", "T"]]
var = {}

for i, j in iterator:
    var[i] = int(f.readline())
    var[j] = [int(k) for k in f.readline().split()]
var["S"] = sorted(var["S"])
var["T"] = sorted(var["T"])

dq = deque(var["S"])
res = 0

for T in var["T"]:
    if T in dq:
        res += 1
        while(dq[0] <= T):
            dq.popleft()
print(res)
