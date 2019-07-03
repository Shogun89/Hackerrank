#include <iostream>
#include <cstdio>
using namespace std;

int main() {
  int my_int;
  long my_long;
  char my_char;
  float my_float;
  double my_double;

  scanf("%d %ld %c %f %lf", &my_int, &my_long,  &my_char, &my_float, &my_double );
  printf("%d\n%ld\n%c\n%f\n%lf", my_int, my_long, my_char, my_float, my_double);
  return 0;
}

