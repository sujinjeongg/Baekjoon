#include <stdio.h>

int main(){
    int N;
    scanf("%d", &N);
    
    int prime[N];
    if(N==1)
        printf("");
    else {
        int i=2,j=0;
        while(N > 1){
            if(N%i == 0){
                prime[j] = i;
                j++;
                N /= i;
            }
            else
                i++;
        }
        
        for(int p=0; p<j; p++)
            printf("%d\n", prime[p]);
    }
    
    return 0;
}