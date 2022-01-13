def solve(i,sm,l,dp,n):
    if(sm == 0):
        return 1
    
    if(i >= n or sm < 0):
        return 0
        
    if(dp[i][sm] != -1):
        return dp[i][sm]
    
        
    if(l[i] <= sm):
        dp[i][sm] = solve(i+1,sm-l[i],l,dp,n) | solve(i+1,sm,l,dp,n)
    else:
        dp[i][sm] = solve(i+1,sm,l,dp,n)
    
    return dp[i][sm]
