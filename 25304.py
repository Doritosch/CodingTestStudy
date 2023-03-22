#구현 - 영수증

price = int(input())

n = int(input())

item = [[0 for _ in range(2)] for _ in range(n)]
sum = 0

for i in range(n) :
    item[i][0],item[i][1] = map(int,input().split())
    sum += (item[i][0] * item[i][1])

if(price == sum) :
    print('Yes')
else :
    print('No')