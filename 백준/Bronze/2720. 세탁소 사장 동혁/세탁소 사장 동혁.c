#include <stdio.h>

int main(){
    int T, C;
    scanf("%d", &T);

    double dollar[4] = {0.25, 0.1, 0.05, 0.01};
    double cent[4] = {0};
    int change[T][4]; //거스름돈

    //거스름돈 각 동전 개수 모두 0으로 초기화
    for(int i=0; i<T; i++)
        for(int j=0; j<4; j++)
            change[i][j] = 0;

    //거스름돈 각 동전 개수 구하기
    for(int i=0; i<T; i++){
        scanf("%d", &C);
        int j=0;
        while(C != 0){
            cent[j] = dollar[j] * 100; //달러를 센트로 변환 (1달러=100센트)
            change[i][j] = C/(int)cent[j];
            C %= (int)cent[j];
            j++;
        }
    }

    for(int i=0; i<T; i++){
        for(int j=0; j<4; j++)
            printf("%d ", change[i][j]);
        printf("\n");
    }

    return 0;
}