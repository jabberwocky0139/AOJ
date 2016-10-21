def BubbleSort(A, N):
    global count
    flag = True
    while flag:
        flag = False
        for j in range(N-1, 0, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                flag = True
                count += 1


def SelectionSort(A):
    global count
    flag = False
    for i in range(len(A)):
        mini = i
        for j in range(i, len(A)):
            if A[j] < A[mini]:
                mini = j
        A[i], A[mini] = A[mini], A[i]
        if i is not mini:
            count += 1
        
N = input()
A = [int(i) for i in input().split()]
count = 0
SelectionSort(A)
print(*A)
print(count)
