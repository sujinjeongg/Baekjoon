#include <stdio.h>

int main(){
    int N;
    scanf("%d", &N);

    int num[N];
    for(int i=0; i<N; i++)
        scanf("%d", &num[i]);

    int temp;
    for(int i=0; i<N; i++)
        for(int j=0; j<N; j++)
            if(num[i] < num[j]){
                temp = num[i];
                num[i] = num[j];
                num[j] = temp;
            }

    for(int i=0; i<N; i++)
        printf("%d\n", num[i]);

    return 0;
}