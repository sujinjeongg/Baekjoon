#include <stdio.h>

int main(){
    int N;
    scanf("%d", &N);
    
    int layer = 1;
    int room = 1;
    if(N==1)
        printf("1");
    else{
        while(room < N){
            room += 6*layer; //room 2~7(6개), 8~19(12개), 20~37(18개)...1st layer, 2st layer..으로 점점 넓혀갈 때 방 수는 6배수로 증가
            layer++;
        }
        printf("%d", layer);
    }
    
    return 0;
}