# [Silver V] 색종이 - 2563 

[문제 링크](https://www.acmicpc.net/problem/2563) 

### 성능 요약

메모리: 1112 KB, 시간: 0 ms

### 분류

구현

### 제출 일자

2024년 8월 3일 21:20:01

### 문제 설명

<p>가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.</p>

<p style="text-align: center;"><img alt="" src="https://u.acmicpc.net/6000c956-1b07-4913-83c3-72eda18fa1d1/Screen%20Shot%202021-06-23%20at%2012.27.04%20PM.png" style="width: 268px; height: 215px;"></p>

<p>예를 들어 흰색 도화지 위에 세 장의 검은색 색종이를 그림과 같은 모양으로 붙였다면 검은색 영역의 넓이는 260이 된다.</p>

### 입력 

 <p>첫째 줄에 색종이의 수가 주어진다. 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 색종이의 수는 100 이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다</p>

### 출력 

 <p>첫째 줄에 색종이가 붙은 검은 영역의 넓이를 출력한다.</p>

### 내가 접근한 방법

잘못한 방법 : 

    #include <stdio.h>

    int main(){
    int N;
    scanf("%d", &N);
    int area = N*100; //넓이

    int x[N], y[N];
    for(int i=0; i<N; i++)
        scanf("%d %d", &x[i], &y[i]);

    //x[i] 값이 작은 수부터 오름차순 나열 (y[i] 값도 x[i]에 따라 오름차순 나열)
    for(int i=1; i<N; i++){
        if(x[i-1] > x[i]){
            int x_temp = x[i];
            x[i] = x[i-1];
            x[i-1] = x_temp;
            int y_temp = y[i];
            y[i] = y[i-1];
            y[i-1] = y_temp;
        }
    }

    //뺄 넓이 구하기
    for(int i=1; i<N; i++)
        if(x[i-1] < x[i] < x[i-1]+10)
            if(y[i-1] < y[i]+10 < y[i-1]+10)
                area -= ((x[i-1]+10)-x[i])*((y[i]+10)-y[i-1]);

    printf("%d", area);

    return 0;
    }
    
색종이끼리 겹친 부분을 전체 N*100 넓이에서 뺐다. x[i]를 오름차순으로 정리하고 y[i]도 x[i] 쌍에 맞게 오름차순으로 정리했다. x부터 x+10까지 부분이 겹칠 때 y부터 y+10까지지 부분도 겹치면 색종이가 겹치는걸로 인식했다. 이렇게 접근하면 코드의 복잡성 문제뿐만 아니라 3개 이상이 겹쳤을 때의 문제점도 생긴다. 
