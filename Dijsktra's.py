from collections import defaultdict
import sys
import heapq as hq
 
def dijkstra(v,s,l,dis):
   
    hq.heapify(v)
    while(v):
        u=extractmin(v)
        
        for j in l[u]:
            b,t,cost=j
            relax(u,b,cost,v,dis)
            
    
 
def relax(u,v,cost,d,dis):
    
    if(dis[u]+cost<dis[v]):
        dis[v]=dis[u]+cost
        hq.heappush(d,[dis[v],v])
 
def extractmin(v):
    x,y=hq.heappop(v)
    return y

  
l=defaultdict(list)
v=[]
for i in range(0,n+1):
    v.append([sys.maxsize,i])
 
v[s][0]=0
 
dis=[sys.maxsize for i in range(n+1)]
dis[s]=0
 
  
