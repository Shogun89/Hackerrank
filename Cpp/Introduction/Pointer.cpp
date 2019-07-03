#include <stdio.h>
#include <stdlib.h>

void update(int *a,int *b) {
       int sum_of_two = *a+*b;
       int abs_diff_of_two = abs(*a-*b);
       *a = sum_of_two;
       *b = abs_diff_of_two;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}

