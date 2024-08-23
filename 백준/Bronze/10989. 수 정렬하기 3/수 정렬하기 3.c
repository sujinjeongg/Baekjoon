#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);

    // 숫자의 범위가 1부터 10,000이므로 10,001 크기의 카운트 배열을 준비합니다.
    int count[10001] = {0};

    // 입력을 받으면서 각 숫자의 빈도를 카운트합니다.
    for (int i = 0; i < N; i++) {
        int num;
        scanf("%d", &num);
        count[num]++;
    }

    // 카운트 배열을 이용하여 정렬된 순서로 출력합니다.
    for (int i = 1; i <= 10000; i++) {
        for (int j = 0; j < count[i]; j++) {
            printf("%d\n", i);
        }
    }

    return 0;
}
