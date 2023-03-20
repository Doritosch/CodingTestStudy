n,cost = map(int,input().split())

count = 0

a= []
for i in range(0,n) :
  num = int(input())
  a.append(num)
a.sort(reverse= True)

for i in a :
  if cost == 0 :
    break
  if cost // i != 0 :
    count += (cost // i)
    cost -= i * (cost // i)
      
print(count)