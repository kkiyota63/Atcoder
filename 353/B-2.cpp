#include <iostream>
using namespace std;

int main(){
    int N,K; // N: 組数, K: 空き席数
    cin >> N >> K;

    int A[K]; // A: 人数
    int seki; // seki: 現在の空き席数
    int ans =0; //ans:発車したバスの数

    for (int i=0;i<N;i++){
        cin >> A[i];
    }

    seki = K;

    //まずは待機列の人数が0でないかを確認し、0ならans+1
    for (int j=0;j<N;j++){
        if(j == N-1){
            ans +=1;
            break;
        }
        else{
            if(A[j]>seki){
                ans += 1; //発車
                seki = K; //リセット
            }
            seki = seki - A[j]; //乗り込む
        }
    }
    cout << ans << endl;

}