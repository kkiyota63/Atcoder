#include <iostream>
using namespace std;

int main(){
    int N, X, Y, Z;
    int flg=0;
    cin >> N >> X >> Y >> Z;

    if(X<Y){
        for (int i=X; i<=Y; i++){
            if(i == Z){
                flg = 1;
            }
        }
    }
    else if(X>Y){
        for (int i=Y; i<=X; i++){
            if(i == Z){
                flg = 1;
            }
        }
    }
    if(flg==1){
        printf("Yes\n");
    }
    else{
        printf("No\n");
    }
    return 0;
}

