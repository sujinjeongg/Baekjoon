#include <stdio.h>
#include <stdlib.h>

// Comparator function for qsort
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int N;
    scanf("%d", &N);

    // Dynamically allocate memory for arrays based on N
    int *before = (int*)malloc(N * sizeof(int));
    int *x = (int*)malloc(N * sizeof(int));
    int *unique = (int*)malloc(N * sizeof(int)); // to store unique sorted elements

    // Input and initialization
    for (int i = 0; i < N; i++) {
        scanf("%d", &x[i]);
        before[i] = x[i];
    }

    // Sort the array x
    qsort(x, N, sizeof(int), compare);

    // Remove duplicates and create the unique sorted array
    int unique_count = 0;
    unique[unique_count++] = x[0]; // The first element is always unique

    for (int i = 1; i < N; i++) {
        if (x[i] != x[i - 1]) {
            unique[unique_count++] = x[i];
        }
    }

    // Output compressed index for each original element in before[]
    for (int i = 0; i < N; i++) {
        int *found = (int*)bsearch(&before[i], unique, unique_count, sizeof(int), compare);
        printf("%ld ", found - unique); // calculate the index of found element
    }

    // Free dynamically allocated memory
    free(before);
    free(x);
    free(unique);

    return 0;
}
