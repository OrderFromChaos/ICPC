#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    int j; // Tracks offset
    vector<int> A;
    A.push_back(1);
    A.push_back(0);
    vector<int> C;
    C.push_back(0);
    C.push_back(1);
    vector<int> D;
    D.push_back(0);
    D.push_back(3);

    for (int i=3; i<=30; ++i) { // Generate in range of allowed input
        j = i-1; // Offset
        A.push_back(D[j-1]+C[j-1]);
        C.push_back(A[j-1]);
        D.push_back(D[j-2]+2*C[j]);
    }

    cin >> n;
    while (n != -1) {
        cout << D[n-1] << endl; // Offset
        cin >> n;
    }

    return 0;
}
