#include <iostream>
using namespace std;

int main(){
    int N,K;
    cin >> N >> K;
    int A[K];
    int seki;
    int ans =1;
    for (int i=0;i<N;i++){
        cin >> A[i];
    }
    seki = K;

    for(int j=0;j<N;j++){
        //A以降が0の場合break
        if(A[j]==0){
            break;
        }
        else{
            if(A[j]>seki){
                seki = K; //席をリセット
                ans +=1;
            }
            if(A[j]<=seki){
                seki = seki - A[j];
            }
        }
    }

    cout << ans << endl;

    return 0;
}