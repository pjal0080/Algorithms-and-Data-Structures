Problem Link : https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/help-ashu-1/
def update(bit,i,val,n):
    while(i<=n):
        bit[i]+=val
        i+=i&(-i)
    
def query(bit,i):
    ans=0
    while(i>0):
        ans+=bit[i]
        i-=i&(-i)
    return ans
    
n=int(input())
l=[int(i) for i in input().split()]
bit=[0]*(n+1)
for i in range(1,n+1):
    update(bit,i,l[i-1]%2,n)
    
 
q=int(input())
for _ in range(q):
    t,x,y=map(int ,input().split())
    if(t==0):
        z=l[x-1]%2
        l[x-1]=y
        k=l[x-1]%2-z
        update(bit,x,k,n)
    if(t==1):
        ans=query(bit,y)-query(bit,x-1)
        print(y-x+1-ans)
    if(t==2):
        ans=query(bit,y)-query(bit,x-1)
        print(ans)
        
