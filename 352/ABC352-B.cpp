#include <iostream>
#include <vector>
using namespace std;

int main() {
    string S, T;
    cin >> S >> T;

    vector<int> ans(S.size(), -1); // -1で初期化し、一致する文字が見つからない場合の値とする
    int j = 0;

    for (int i = 0; i < T.size(); i++) {
        if(S[j]==T[i]){
            ans[j] = i;
            j++;
        }
    }

    for (int i = 0; i < S.size(); i++) {
        cout << ans[i]+1 << " "; // cntの値を出力する
    }
    cout << endl;

    return 0;
}