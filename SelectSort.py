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
