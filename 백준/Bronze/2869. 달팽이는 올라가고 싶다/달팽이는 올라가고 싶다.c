#include <stdio.h>

int main(){
    int A, B, V;
    scanf("%d %d %d", &A, &B, &V);
    
    int day_height = A - B; //하루동안 올라가는 높이
    int goal_height = V - B; //마지막날에는 올라가기만 하고 미끄러지지 않음
    
    int day = goal_height / day_height;
    if(goal_height % day_height != 0) //나누어 떨어지지 않으면
        day++;
    
    printf("%d", day);
    
    return 0;
}