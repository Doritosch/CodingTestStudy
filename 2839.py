#설탕 배달
#최대한 적은 봉지 배달, 봉지 - 3kg, 5kg

n = int(input()) #kg 

count = 0
 
while n >= 0 :
  if n % 5 == 0 : 
    count += n / 5
    n = 0 
    break
  else :
    n -= 3
    count += 1
    
  
if n == 0 :
  print(int(count))
else : 
  print('-1')