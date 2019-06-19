
def build(stree,st,end,index,l):
    if(st>end):
        return

    if(st==end):
        stree[index]=l[st]
        return

    mid=(st+end)//2
    build(stree,st,mid,2*index,l)
    build(stree,mid+1,end,2*index+1,l)

    stree[index]=stree[2*index] + stree[2*index+1]


def update(stree,st,end,index,i,val):
    if(i<st or i>end):
        return

    if(st==end):
        stree[index]=val
        return

    mid=(st+end)//2
    update(stree,st,mid,2*index,i,val)
    update(stree,mid + 1,end,2*index+1,i,val)

    stree[index] = stree[2*index] + stree[2*index+1]



def query(stree,st,end,index,lt,rt):
    if(rt<st or lt>end):
        return 0

    if(lt<=st and rt>=end):
        return stree[index]

    mid=(st+end)//2
    left = query(stree,st,mid,2*index,lt,rt)
    right = query(stree,mid+1,end,2*index+1,lt,rt)

    return left+right






n=int(input())
l=[int(i) for i in input().split()]
stree=[0 for i in range(0,2*n+4)]
st=0
end=n-1
index=1
build(stree,st,end,index,l)

q=int(input())
for _ in range(q):
    a=[int(i) for i in input().split()]
    if(a[0]==1):
        update(stree,0,n-1,1,a[1],a[2])
    else:
        ans = query(stree,0,n-1,1,a[1],a[2])
        print(ans)
