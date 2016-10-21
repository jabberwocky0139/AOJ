# coding: utf-8

def bubbleSort(A, N):
    global count
    flag = True
    while flag:
        flag = False
        for j in range(N-1, 0, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                flag = True
                count += 1

N = int(input())
A = [int(i) for i in input().split()]
count = 0
bubbleSort(A, N)
print(A)
print(count)
