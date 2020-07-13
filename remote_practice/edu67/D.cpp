#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

template <class T>
void printVector(vector<T> V) {
    for (T val: V) {
        cout << val << " ";
    }
    cout << endl;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N;
        vector<int> A, B;
        int Bprev = N+1;
        int Atop, Btop;
        unordered_map<int, int> Abuf, Bbuf;
        bool orderfail = false;

        cin >> N;
        int temp;
        for (int x = 0; x < N; x++) {
            cin >> temp;
            A.push_back(temp);
        }
        for (int x = 0; x < N; x++) {
            cin >> temp;
            B.push_back(temp);
        }
        // printVector(A);
        // printVector(B);

        for (int n = N-1; n >= 0; n--) {
            Atop = A[n];
            Btop = B[n];
            if (Atop != Btop) {
                Abuf[Atop] += 1; // Works because default int constructor is 0
                Bbuf[Btop] += 1;

                if (Btop > Bprev) {
                    // cout << "Failed because " << Btop << " > " << Bprev << endl;
                    orderfail = true;
                    break;
                } else {
                    Bprev = Btop;
                }
            }
        }

        if (!orderfail) {
            if (Abuf.size() > 0) {
                bool nextQuery = false;
                for (pair<int, int> p : Abuf) {
                    // cout << '(' << p.first << ", " << p.second << ')' << endl;
                    if (Bbuf.count(p.first) > 0) {
                        if (Bbuf[p.first] != p.second) {
                            // cout << "Non-matching terms frequencies are not identical" << endl;
                            cout << "NO" << endl;
                            nextQuery = true;
                        }
                    } else {
                        // cout << "Term in A array does not exist in B array: \"" << p.first << "\"" << endl;
                        cout << "NO" << endl;
                        nextQuery = true;
                    }
                }
                if (nextQuery) {
                    continue;
                } else {
                    // cout << "Abuf == Bbuf" << endl;
                    cout << "YES" << endl;
                }
            } else {
                // cout << "Buffer is empty, so strings already match" << endl;
                cout << "YES" << endl;
            }
        } else {
            // cout << "Non-matching B terms are in decreasing order" << endl;
            cout << "NO" << endl;;
        }
        
    }

    return 0;
}


