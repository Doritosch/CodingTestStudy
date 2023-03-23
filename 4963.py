# DFS - 섬의 개수
import sys
sys.setrecursionlimit(10**4)

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(x,y,w,h) :
    island[y][x] = 2    #방문표시
    for k in range(8) :
        nx,ny = x + dx[k], y + dy[k]
        if 0 <= nx < w and 0 <= ny < h :
            if island[ny][nx] == 1 :
                dfs(nx,ny,w,h)
    return 1

while True :
    w, h = map(int,input().split())
    
    if w == 0 and h == 0 :  #종료 조건 
        break
    
    island = [list(map(int,input().split())) for _ in range(h)]
    sum = 0
    for i in range(h) :
        for j in range(w) :
            if island[i][j] == 1 :
               sum += dfs(j,i,w,h)
    
    print(sum)