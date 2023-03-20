#ATM
n = int(input())
p = list(map(int,input().split()))

p.sort()

sum = 0

for i in range(0,n) :
  sum += p[i]
  for k in range(0,i) :
   sum += p[k]
    
print(sum)