from bisect import bisect_left as bl
n = int(input())
l = [int(i) for i in input().split()]
ans=[l[0]]
for i in range(1,n):
    if(l[i]>ans[-1]):
        ans.append(l[i])
    else:
        x=bl(ans,l[i])
        if(x>0):
	    
            if(l[i]-ans[x-1]>0):	
                ans[x]=l[i]
        else:
            ans[x]=l[i]
    
print(len(ans))
