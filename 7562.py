# BFS - 나이트의 이동

from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    
    while queue :
        x,y = queue.popleft()
        
        if x == end_x and y == end_y :
            return board[x][y]
        
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n :
                continue
            if board[nx][ny] == 0 :
                board[nx][ny] = board[x][y] + 1
                queue.append((nx,ny))
            
                
            
N = int(input())

for i in range(N) :
    n = int(input())
    board = [[0 for j in range(n)] for i in range(n)]
    start_x, start_y = map(int,input().split())
    end_x, end_y = map(int,input().split())
    print(bfs(start_x,start_y))