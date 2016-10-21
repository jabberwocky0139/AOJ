def merge(A, left, mid, right):
  global counter
  n1, n2 = mid - left, right - mid
  L, R = list(A[left:left+n1]+[float("inf")]), list(A[mid:mid+n2]+[float("inf")])
  i = j = 0
  for k in range(left, right):
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1
  counter += right - left
def mergeSort(A, left, right):
  if left+1 < right:
    mid = (left + right)//2;
    mergeSort(A, left, mid)
    mergeSort(A, mid, right)
    merge(A, left, mid, right)

N = int(input())
A = [int(i) for i in input().split()]
counter = 0
mergeSort(A, 0, len(A))
print(*A)
print(counter)
