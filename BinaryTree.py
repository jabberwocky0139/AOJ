# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, N):
        self.parent = [-1 for i in range(N)]
        self.left = [-1 for i in range(N)]
        self.right = [-1 for i in range(N)]
        self.depth = [-1 for i in range(N)]
        self.sibling = [-1 for i in range(N)]
        self.height = [0 for i in range(N)]
        self.degree = [0 for i in range(N)]

    def set_depth(self, u):
        d, U = 0, u
        while T.parent[u] is not -1:
            u = T.parent[u]
            d += 1
        self.depth[U] = d

    def set_height(self, u):
        h1 = h2 = 0
        if self.left[u] is not -1:
            h1 = self.set_height(self.left[u]) + 1
        if self.right[u] is not -1:
            h2 = self.set_height(self.right[u]) + 1
        
        self.height[u] = max(h1, h2)
        return max(h1, h2)
            

# テストは上. 提出時は下
FILE = open("input.txt")
N = int(FILE.readline())
## N = int(input())

# create node
T = Node(N)

# set data
for j in range(N):
    # テストは上. 提出時は下
    A = [int(i) for i in FILE.readline().split()]
    ## A = [int(i) for i in input().split()]

    # left・rightの決定
    T.left[A[0]] = A[1]
    T.right[A[0]] = A[2]
    
    # parent・degreeの決定
    for u in A[1:]:
        if u is not -1:
            T.parent[u] = A[0]
            T.degree[A[0]] += 1
            
    # siblingの決定
    if (A[1] is not -1) and (A[2] is not -1):
        T.sibling[A[1]], T.sibling[A[2]] = A[2], A[1]

# set depth
for i in range(N):
    T.set_depth(i)

# set height
T.set_height(T.parent.index(-1))

# 出力
for i in range(N):
    # ノードの種類を分類
    if T.parent[i] is -1:
        node = "root"
    elif T.left[i] is -1 and T.right[i] is -1:
        node = "leaf"
    else:
        node = "internal node"

    print("node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}".format(i, T.parent[i], T.sibling[i], T.degree[i], T.depth[i], T.height[i], node))
