#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    
    int H[N];
    for (int i = 0; i < N; i++) {
        cin >> H[i];
    }
    
    int ans = 0;
    bool flg = false;
    
    for (int j = 1; j < N; j++) {
        if (H[j] > H[0]) {
            ans = j + 1;
            flg = true;
            break;
        }
    }
    
    if (flg) {
        cout << ans << endl;
    } else {
        cout << -1 << endl;
    }
    
    return 0;
}