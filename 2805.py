# 이진 탐색 - 나무 자르기

import sys
input = sys.stdin.readline

def binary_search(array = list(), target = int(), left = int(), right = int()) : 
    if left > right :
        return right
    
    mid = (left + right) // 2
    
    cnt =  0
    for i in array :
        if mid < i :
            cnt += i - mid

    if cnt >= target :
        return binary_search(array, target,mid + 1, right)
    else : 
        return binary_search( array, target, left, mid -1)

N, M = map(int,input().split())

tree = list(map(int,input().split()))
tree.sort()

print(binary_search(tree, M, 1, max(tree)))

#문제 발생 : output에서 1 차이로 오답인 상황 발생
#해결 - 조건문 잘 확인하자