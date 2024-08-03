#include <stdio.h>

int main(){
    int N=0;
    scanf("%d", &N);

    int x, y;
    int canvas[100][100] = {0}; //도화지
    //색종이가 있는 부분 1로 표시하기
    for(int i=0; i<N; i++){
        scanf("%d %d", &x, &y);
        for(int p=0; p<10; p++)
            for(int q=0; q<10; q++)
                canvas[x+p][y+q] = 1; 
    }
    
    int black_area = 0;
    //2차원 배열에서 1로 표시된 영역 수(넓이) 세기
    for(int i=0; i<100; i++)
        for(int j=0; j<100; j++)
            if(canvas[i][j] == 1)
                black_area ++;
            
    printf("%d", black_area);

    return 0;
}