# 1764 - 듣보잡
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

no_listen = set([str(input()) for _ in range(N)])
answer = [input_str for input_str in (str(input()) for _ in range(M)) if input_str in no_listen]

count = len(answer)

print(count)

for name in sorted(answer) :
    print(name.strip())