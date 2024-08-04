#include <stdio.h>
#include <string.h>
#include <math.h>

//문자로 입력 받고 숫자로 변환
int charToint(char c){
    if(c >= '0' && c <= '9')
        return c - '0';
    else
        return c - 'A' + 10; //A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
}

int main(){
    char N[32];
    int B;
    scanf("%s %d", N, &B);

    int length = strlen(N);
    int result = 0;
    //문자를 숫자로 변환 후 진법 계산
    for(int i=0; i<length; i++) 
        result += charToint(N[i]) * pow(B, (length-1)-i);
    
    printf("%d", result);
    return 0;
}