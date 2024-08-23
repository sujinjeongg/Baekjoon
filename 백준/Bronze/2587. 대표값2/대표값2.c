#include <stdio.h>

int main(){
    int num[5];
    int sum = 0;
    
    for(int i=0; i<5; i++){
        scanf("%d", &num[i]);
        sum += num[i];
    }
    
    for(int i=0; i<5; i++)
        for(int j=0; j<5; j++)
            if(num[i] < num[j]){
                int temp = num[i];
                num[i] = num[j];
                num[j] = temp;
            }
    
    int mean = sum/5;
    int medium = num[2];
    
    printf("%d\n%d", mean, medium);

    return 0;
}