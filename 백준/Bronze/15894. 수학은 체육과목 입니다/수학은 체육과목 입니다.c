#include <stdio.h>

int main(){
    long int n; //int는 20억까지인데 결과값은 10^9*4=최대40억이 나올 수 있음
    scanf("%ld", &n);

    printf("%ld", n*4);
    
    return 0;
}