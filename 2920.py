#구현 - 음계

n = list(map(int,input().split()))

if (n[0] == 1) :
    for i in range(len(n)-1) :
        if (n[i] != n[i+1] - 1) :
            print('mixed')
            exit()
    print('ascending')
elif (n[0] == 8) :
    for i in range(len(n)-1) :
        if (n[i] != n[i+1] + 1) :
            print('mixed')
            exit()
    print('descending')
else :
    print('mixed')
        