# 정렬 - 좌표 정렬하기
import sys
input = sys.stdin.readline

n = int(input())
dot = [list(map(int,list(input().split())))for _ in range(n)]

dot.sort()

for i in range(n) :
    print(dot[i][0],dot[i][1])