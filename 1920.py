# 이진 탐색 - 수 찾기

import sys
input = sys.stdin.readline

def binary_search(array = list(), target = int(), left = int(), right = int()) :
    
    if left > right :
        return 0
    
    mid = (left + right) // 2
    
    if target == array[mid] :
        return 1
    elif target > array[mid] :
        return binary_search(array = array, target = target, left = mid+1, right = right)
    else :
        return binary_search(array = array, target = target, left = left, right = mid -1)
    
N = int(input())

A = list(map(int,input().split()))
A.sort()

M = int(input())

C = list(map(int,input().split()))

for i in range(len(C)) :
    C[i] = binary_search(array = A,target = C[i],left = 0, right = len(A) - 1)

for i in range(len(C)) :
    print(C[i])