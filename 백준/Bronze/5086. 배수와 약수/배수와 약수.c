#include <stdio.h>

int main() {
    int a, b;
    char results[100][10]; // 결과를 저장할 배열, 최대 100개의 테스트 케이스를 가정
    int i = 0; // 결과 배열의 인덱스

    // 입력을 계속 받음
    while (1) {
        scanf("%d %d", &a, &b);

        // 입력이 0 0인 경우 반복문 종료
        if (a == 0 && b == 0) {
            break;
        }

        // 첫 번째 숫자가 두 번째 숫자의 약수인지 확인
        if (b % a == 0) {
            sprintf(results[i], "factor");
        }
        // 첫 번째 숫자가 두 번째 숫자의 배수인지 확인
        else if (a % b == 0) {
            sprintf(results[i], "multiple");
        }
        // 둘 다 아닌 경우
        else {
            sprintf(results[i], "neither");
        }

        i++; // 결과 배열의 인덱스를 증가
    }

    // 저장된 결과를 한 번에 출력
    for (int j = 0; j < i; j++) {
        printf("%s\n", results[j]);
    }

    return 0;
}

