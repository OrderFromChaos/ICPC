#include <iostream>
#include <cmath>

using namespace std;

int main() {
  for(int i = 0; i < 10000; ++i) {
    int implicitcast = (int)(pow(i,5) + 0.5);
    int moderncast = static_cast<int>(pow(i,2));
    if (implicitcast != moderncast) {
        cout << implicitcast << ' ' << moderncast << endl;
    }
  }
  return 0;
}