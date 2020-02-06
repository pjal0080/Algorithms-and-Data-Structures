#include <bits/stdc++.h>
using namespace std;
#define FOR(k,n) for(int i=k;i<(n);i++)
typedef vector<int> vi;
#define pb push_back
const int LG = 20;
const int N = 200005;

vi l[N];
int par[N][LG];
int lvl[N];


void dfs(int u,int pa){
    lvl[u] = 1 + lvl[pa];
    par[u][0] = pa;

    for(int v : l[u]){
        if(v == pa)
        continue;

        dfs(v,u);

    }

}

int lca(int u,int v){

    int lg = 0;

    if(lvl[u] < lvl[v]){
        u = u + v;
        v = u - v;
        u = u - v;

    }


    while((1<<lg) <= lvl[u])
        lg += 1;

    lg -= 1;

    for(int i = lg;i >=0;i--){
        if(lvl[u] - (1<<i) >= lvl[v])
            u = par[u][i];
    }

    if(u == v)
        return u;

    for(int i = lg;i >=0;i--){

           if(par[u][i] != -1 && par[u][i] != par[v][i]){
                u = par[u][i];
                v = par[v][i];

        }

    }

    return par[u][0];

}


int main() {

	ios_base :: sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin>>n;
	int u,v;

	FOR(0,n-1){
	    cin>>u>>v;
        l[u].pb(v);
        l[v].pb(u);
	}


    for(int i = 0;i<LG;i++){

        for(int j = 0;j<=n;j++){
            par[j][i] = -1;
        }
    }

    lvl[0] = -1;

    dfs(1,0);

    for(int i = 1;i<LG;i++){
        for(int j = 1;j<=n;j++){
            if(par[j][i-1] != -1)
                par[j][i] = par[par[j][i-1]][i-1];
        }
    }

    int q,r,x,y;
    cin>>q;
    while(q--){
        cin>>r>>x>>y;

        int a = lca(x,y);
        int b = lca(r,x);
        int c = lca(r,y);

        if(a == b)
            cout<< c <<endl;
        else if(b == c)
            cout<< a << endl;
        else
            cout<< b<<endl;


    }

	return 0;
}
