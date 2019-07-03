#include <iostream>
#include <cstdio>
#include <valarray>
using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/

int max_of_four(int a, int b, int c, int d) {
  int nums[] = {a, b, c, d};
  valarray<int> valArr(nums, 4);
  return valArr.max();
}

int main(){

    int a,b,c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int result = max_of_four(a,b,c,d);
    printf("%d", result);
}

