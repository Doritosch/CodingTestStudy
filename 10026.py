# DFS - 적록색약
import copy
import sys
sys.setrecursionlimit(10**6)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x,y, n, color) :
    board1[y][x] = 'C'   #방문표시
    for k in range(4) :
        nx,ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n :
            if board1[ny][nx] == color:
                dfs(nx,ny,n,color)
    return 1

def blindness_dfs(x,y, n, blind_color) :
    board2[y][x] = 'C'   #방문표시
    for k in range(4) :
        nx,ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n :
            if (blind_color == 'R' or blind_color =='G') and (board2[ny][nx] == 'R' or board2[ny][nx] == 'G') :
                blindness_dfs(nx,ny,n,blind_color)
            elif board2[ny][nx] == blind_color :
                blindness_dfs(nx,ny,n,blind_color)   
    return 1

n = int(input())

board1 = [list(map(str,list(input()))) for _ in range(n)]
board2 = copy.deepcopy(board1)

normal = 0  #평범
blindness = 0   #색약
for i in range(n) :
    for j in range(n) :
        if board1[i][j] != 'C' :
            color = board1[i][j]
            normal += dfs(j,i,n,color)
        if board2[i][j] != 'C' :
            blind_color = board2[i][j]
            blindness += blindness_dfs(j,i,n,blind_color)

print(normal,blindness)