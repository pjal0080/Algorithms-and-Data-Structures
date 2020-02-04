#include<iostream>
using namespace std;
#define mod 1000000007
void matmul(long long A[2][2],long long B[2][2]){
    long long C[2][2];
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            C[i][j] = 0;
            for (int k = 0; k < 2; k++)
            {
                long long temp=((A[i][k]%mod)*(B[k][j]%mod))%mod;
                C[i][j] = ((C[i][j]%mod)+(temp%mod))%mod;
            }
        }
    }
    for (int i=0; i<2; i++)
        for (int j=0; j<2; j++)
            A[i][j] = C[i][j]%mod;  
}
 
long long modex(long long A[2][2],long long n){
    long long M[2][2] ={{1,1},{1,0}};
    if(n==1){
       return A[0][0]*2+A[0][1];
    }
    modex(A,n/2);
    
    matmul(A,A);
    
    if(n%2!=0){
        matmul(A,M);
    }
    return (A[0][0]*2 + A[0][1])%mod ;
}
    
 
 
int main(){
    int t;
    cin>>t;
    while(t--){
        long long n;
        cin>>n;
        if(n==1)
         cout<<'2'<<endl;
        else{
            
        
        long long A[2][2]={{1,1},{1,0}};
        long long res=modex(A,n-1);
        cout<<res%mod<<endl;
        }
    }
    
    return 0;
    
}

