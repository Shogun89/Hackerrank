#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void PrintArr(int arr[], int count){
    for(int i = 0; i < count; i++)
        cout << arr[i] << ' ';

    cout << '\n';

}

void reverse(int arr[], int count){
    int place;

    for (int i = 0; i < count/2; i++){
        place = arr[i];
        arr[i] = arr[count-i-1];
        arr[count-i-1] = place;

    }


}

int main() {
    int n;
    cin >> n;
    
    int arr[n];
    
    for ( int i =0; i < n;i++){
        int place;
        cin >> place;
        arr[i] = place;

    }

    reverse(arr,n);

    PrintArr(arr,n);
    return 0;
}
