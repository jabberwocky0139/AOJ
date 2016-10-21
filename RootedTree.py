# -*- coding: utf-8 -*-
# -*- Head for READABLE CODE -*- #
# -*- One method, one comment -*- #
import sys

# 再帰の深さの最大値を上げないとRuntimeErrorを吐かれる(デフォルトは1000)
# 深さを上げても深すぎるとどうせcore dunpする
## sys.setrecursionlimit(100000)

class Node(object):
    # leftが存在しないのが葉(leaf), rightがs存在しないのが最も右の子
    # 親・右の子・左の子が存在しない場合はparentを-1にする
    def __init__(self, N):
        self.p = [-1 for i in range(N)]
        self.l = [-1 for i in range(N)]
        self.r = [-1 for i in range(N)]
        self.D = [0 for i in range(N)]

    # 未使用. Pythonで再帰は2sで通らない
    def set_depth_rec(self, u, p):
        self.D[u] = p
        if self.r[u] is not -1:
            self.set_depth_rec(self.r[u], p)
        if self.l[u] is not -1:
            self.set_depth_rec(self.l[u], p+1)

    # もっと効率よくできるが, これでも1sくらいで通る
    def set_depth(self, u):
        d = 0
        pre_u = u
        while self.p[u] is not -1:
            u = self.p[u]
            d += 1
        self.D[pre_u] = d

    # ノードに対して子のリストを返す. 
    def return_children(self, u):
        children = []
        flag = self.l[u]
        while flag is not -1:
            children.append(flag)
            flag = self.r[flag]

        return children

# テストは上. 提出時は下
f = open("input.txt")
N = int(f.readline())
## N = int(input())

# ノードの生成
T = Node(N)

# ノードの値をleft-child, right-sibling representationで格納
for j in range(N):
    # テストは上. 提出時は下
    A = [int(i) for i in f.readline().split()]
    ## A = [int(i) for i in input().split()]
    
    # leftの決定
    if len(A) > 2:
        T.l[A[0]] = A[2]
    else:
        T.l[A[0]] = -1
    
    # parent・rightの決定
    for index, i in enumerate(A[2:]):
        if(A[-1] == i):
            T.p[i], T.r[i] = A[0], -1
        else:
            T.p[i], T.r[i] = A[0], A[index+3]

# 各ノードの深さを調べる. 再帰はcore dump
## T.set_depth_rec(T.p.index(-1), 0)
for i in range(N):
    T.set_depth(i)

# ノードの種類を分類
for i in range(N):
    if T.p[i] is -1:
        node = "root"
    elif T.l[i] is -1:
        node = "leaf"
    else:
        node = "internal node"

    # 出力
    print("node {0}: parent = {1}, depth = {2}, {3}, {4}".format(i, T.p[i], T.D[i], node, T.return_children(i)))
