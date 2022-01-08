# Problem - Count ways to make N from 2 and 4(Order does not matter)

def solve(n):
    if(n % 2 != 0):
        return 0
    
    if(n < 2):
        return 0
    
    if(n == 3):
        return 0
        
    return (n//4) + 1




n = int(input())
l = list(map(int ,input().split()))
for i in range(n):
    print(solve(l[i]))
