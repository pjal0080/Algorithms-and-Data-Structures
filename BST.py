Problem Link : https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/dummy3-4/description/
class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
 
def insert(root,data):
    if(root==None):
        root=node(data)
    else:
        if(root.data>data):
            if(root.left == None):
                root.left = node(data)
            else:
                insert(root.left,data)
            
        else:
            if(root.right is None):
                root.right = node(data)
            else:
                insert(root.right,data)
            
           
            
def getheight(root):
    if(root==None):
        return 0
    else:
        return max(getheight(root.left),getheight(root.right))+1
t=int(input())
for _ in range(t):
    n=int(input())
    l=[int(i) for i in input().split()]
    t=node(l[0])
    for i in range(1,n):
        insert(t,l[i])
    x=getheight(t)
    print(x)
