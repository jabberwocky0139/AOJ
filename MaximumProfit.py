# coding: utf-8
N = int(input())
input_line = []
for i in range(N):
    input_line.append(int(input()))

maxv = input_line[1] - input_line[0]
minv = input_line[0]
for j in range(1, N):
    maxv = max(maxv, input_line[j] - minv)
    minv = min(minv, input_line[j])
print(maxv)
