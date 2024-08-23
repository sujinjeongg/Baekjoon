#include <stdio.h>
#include <stdlib.h>

// Comparator function for qsort
int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    int N;
    scanf("%d", &N);
    
    int x[N];
    for (int i = 0; i < N; i++)
        scanf("%d", &x[i]);

    // Using qsort from stdlib.h
    qsort(x, N, sizeof(int), compare);

    for (int i = 0; i < N; i++)
        printf("%d\n", x[i]);

    return 0;
}
