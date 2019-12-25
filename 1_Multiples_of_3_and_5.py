import sys

def muplipleOrNot(num):
    if((num % 15 ==0) | (num % 5 ==0) | (num % 3 ==0)):
        return 1
    else:
        return 0

t = int(input().strip())
sumList = []
for a0 in range(t):
    n = int(input().strip())
    sum = 0
    for num in range(n):
        divisible = muplipleOrNot(num)
        if(divisible == 1):
            sum += num
    sumList.append(sum)

[print(sum) for sum in sumList]