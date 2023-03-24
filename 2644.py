# BFS - 촌수계산

from collections import deque

def bfs(first,visited) :
    queue = deque()
    queue.append(first)
    
    while queue :
        v = queue.popleft()
        
        for i in pedigree[v] :
            if visited[i] == 0 :
                visited[i] = visited[v] + 1
                queue.append(i)
    return visited[end]
            

N = int(input())
pedigree = [[] for i in range(N+1)]

start,end = map(int,input().split())
n = int(input())
for i in range(n) :
    p, q = map(int,input().split())
    pedigree[p].append(q)
    pedigree[q].append(p)
     
visited = [0] * (N+1)

if bfs(start,visited) != 0 :  
    print(bfs(start,visited))
else :
    print(-1)