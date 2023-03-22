#구현 - 다이얼

word = input()
sum = 0

for i in range(len(word)) :
    if(ord(word[i]) < 80) :
        sum += (ord(word[i]) % ord('A')) // 3 + 3
    elif word[i] in ['P','Q','R','S'] :
        sum += 8
    elif word[i] in ['T','U','V'] :
        sum += 9
    else : 
        sum += 10
    
print(sum)