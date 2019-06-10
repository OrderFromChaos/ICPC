#include <iostream>
#include <string>
using namespace std;

int main() {
    string z = "Yes.";
    for (int i = 0, int j = 0; i < z.length(); ++i, ++j ) {
        cout << i << endl;
        cout << j << endl;
    }
    return 0;
}
