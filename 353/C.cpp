#include <iostream>
using namespace std;

//xとyの和を10^8で割った余りを返す関数
long long func(long long x, long long y) {
    return (x + y) % (100000000);
}

int main() {
    int N;
    cin >> N;

    const int MAX_SIZE = 100; // 適切な値に変更
    int A[MAX_SIZE];

    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    long long ans = 0; // 値が大きくなる可能性があるので long long 型を使う
    for (int i = 0; i < N - 1; i++) {
        for (int j = i + 1; j < N; j++) {
            ans += func(A[i],A[j]); 
        }
    }

    cout << ans << endl;
    return 0;
}