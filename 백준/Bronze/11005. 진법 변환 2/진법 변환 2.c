#include <stdio.h>
#include <string.h>
#include <math.h>

int main(){
    int N, B;
    scanf("%d %d", &N, &B);

    int remainder[100] = {0};//나머지
    int i=0;
    //소인수분해
    while(N >= B){
        remainder[i] = N%B;
        N /= B;
        i++;
    }
    remainder[i] = N;

    for(int j=i; j>=0; j--){
        if(remainder[j] >= 0 && remainder[j] <= 9)
            printf("%d", remainder[j]);
        else
            printf("%c", (remainder[j]-10)+'A');
    }

    return 0;
}