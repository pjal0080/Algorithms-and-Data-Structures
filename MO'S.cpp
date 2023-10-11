Problem Link : http://codeforces.com/contest/86/problem/D
#include<bits/stdc++.h>
using namespace std;
#define block 447
#define N 200001
#define ll long long
int n,t;
int a[N];
struct query{
    int left,right,i;
}q[N];
 
ll ans = 0;
int cnt[1000001];
 
bool cmp(query x,query y){
    if(x.left/block != y.left/block)
        return x.left < y.left;
 
    return x.right > y.right;
 
}
 
int main(){
    int max = -1;
    scanf("%d %d",&n,&t);
    for(int i=0;i<n;i++){
        scanf("%d ",&a[i]);
        if(max < a[i])
         max = a[i];
    }
    for(int i = 0 ;i < t;i++){
    cin >> q[i].left >>q[i].right;
    q[i].left--;
    q[i].right--;
    q[i].i = i;
 
}
sort(q,q+t,cmp);
 
for(int i = 0;i<=max;i++){
    cnt[i] = 0;
}
int curl = 0;
int curr = -1;
ll res[t+1];
for(int i = 0; i < t; i++){
    int l = q[i].left;
    int r = q[i].right;
 
    while(curr < r){
        curr++;
        if(cnt[a[curr]] == 0){
            cnt[a[curr]]++;
            ans +=  cnt[a[curr]] * cnt[a[curr]] * a[curr];
        }
 
        else{
          cnt[a[curr]]++;
          ans += (2*cnt[a[curr]] - 1) * a[curr];
        }
    }
 
 
    while(curr > r){
 
        if(cnt[a[curr]] == 1){
            ans -=  cnt[a[curr]] * cnt[a[curr]] * a[curr];
            cnt[a[curr]]--;
        }
 
        else{
            cnt[a[curr]]--;
            ans -= (2*cnt[a[curr]] + 1) * a[curr];
        }
        curr--;
    }
 
    while(curl > l){
        curl--;
        if(cnt[a[curl]] == 0){
            cnt[a[curl]]++;
            ans +=  cnt[a[curl]] * cnt[a[curl]] * a[curl];
 
        }
 
        else{
            cnt[a[curl]]++;
            ans += (2*cnt[a[curl]] - 1) * a[curl];
        }
 
    }
    while(curl < l){
        if(cnt[a[curl]] == 1){
            ans -=  cnt[a[curl]] * cnt[a[curl]] * a[curl];
            cnt[a[curl]]--;
        }
 
        else{
            cnt[a[curl]]--;
            ans -= (2*cnt[a[curl]] + 1) * a[curl];
        }
 
        curl++;
    }
    res[q[i].i] = ans;
}
for(int i =0 ;i < t; i++){
    cout<<res[i]<<endl;
}
 
return 0;
}
