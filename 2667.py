# DFS - 단지번호붙이기

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x,y,n) :
    global sum
    apart[y][x] = 2    #방문표시
    for k in range(4) :
        nx,ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n :
            if apart[ny][nx] == 1 :
                sum += 1
                dfs(nx,ny,n)
    return 1

n = int(input())
count = 0
complex = []    #단지

apart = [list(map(int,list(input()))) for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        if apart[i][j] == 1 :
          sum = 1
          count += dfs(j,i,n)
          complex.append(sum)

complex.sort()

print(count)
for i in range(len(complex)) :
    print(complex[i])