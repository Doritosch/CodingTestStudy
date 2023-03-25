# 정렬 - 생일
import sys
input = sys.stdin.readline

n = int(input())

info = [list(map(str,input().split())) for _ in range(n)]

info.sort(key = lambda x : (int(x[3]), int(x[2]), int(x[1])))
print(info[len(info)-1][0])
print(info[0][0])