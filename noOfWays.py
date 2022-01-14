def solve(i,n,s,sz,dp,prev):
    
    if(n == 3):
        return 1
    
    if(i >= sz):
        return 0
    
    if(dp[i][n][prev] != 0):
        return dp[i][n][prev]
    
    if(int(s[i]) ^ prev == 1 or n == 0):
        dp[i][n][prev] = solve(i+1,n+1,s,sz,dp,int(s[i])) + solve(i+1,n,s,sz,dp,prev)
    
    else:
        dp[i][n][prev] = solve(i+1,n,s,sz,dp,prev)
        
    
    return dp[i][n][prev]
    
l = list(input().split())
for i in range(len(l)):
    n = len(l[i])
    dp = [[[0 for i in range(2)] for j in range(4)] for k in range(n)]
    prev = 0
    solve(0,0,l[i],n,dp,prev)
    print(dp[0][0][0])
