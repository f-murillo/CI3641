#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_SIZE (1024L * 1024L * 1024L * 2) // 2 GB máximo permitido para esta prueba

// Función para inicializar la matriz con valores aleatorios
void initialize_matrix(double **matrix, int N, int M) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            matrix[i][j] = rand() % 1000; // Valores aleatorios entre 0 y 999
        }
    }
}

// Suma por filas
double sum_by_row(double **matrix, int N, int M) {
    double sum = 0.0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            sum += matrix[i][j];
        }
    }
    return sum;
}

// Suma por columnas
double sum_by_column(double **matrix, int N, int M) {
    double sum = 0.0;
    for (int j = 0; j < M; ++j) {
        for (int i = 0; i < N; ++i) {
            sum += matrix[i][j];
        }
    }
    return sum;
}

// Función principal para medir el tiempo de ejecución y exportar a CSV
int main() {
    int sizes[] = {100, 1000, 10000}; // Tamaños de la matriz ajustados
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);
    int repetitions = 3; // Número de veces que se ejecutará cada configuración
    FILE *fp = fopen("resultados.csv", "w");

    if (fp == NULL) {
        printf("Error al abrir el archivo para escribir.\n");
        return 1;
    }

    // Escribir encabezados en el archivo CSV
    fprintf(fp, "Tamaño,Repetición,Tiempo (sum_by_row),Tiempo (sum_by_column)\n");

    for (int k = 0; k < num_sizes; ++k) {
        int N = sizes[k];
        int M = sizes[k];

        // Comprobar si la matriz cabe en memoria
        if ((long long)N * M * sizeof(double) > MAX_SIZE) {
            printf("Matriz de tamaño %d x %d no cabe en memoria.\n", N, M);
            continue;
        }

        for (int r = 0; r < repetitions; ++r) {
            // Reserva de memoria para la matriz
            double **matrix = (double **)malloc(N * sizeof(double *));
            if (matrix == NULL) {
                printf("Error al asignar memoria para la matriz de tamaño %d x %d.\n", N, M);
                exit(EXIT_FAILURE);
            }
            for (int i = 0; i < N; ++i) {
                matrix[i] = (double *)malloc(M * sizeof(double));
                if (matrix[i] == NULL) {
                    printf("Error al asignar memoria para la matriz de tamaño %d x %d.\n", N, M);
                    exit(EXIT_FAILURE);
                }
            }

            // Inicializar la matriz
            initialize_matrix(matrix, N, M);

            // Medir el tiempo de ejecución para recorrer por filas
            struct timespec start, end;
            clock_gettime(CLOCK_MONOTONIC, &start);
            double sum = sum_by_row(matrix, N, M);
            clock_gettime(CLOCK_MONOTONIC, &end);
            double time_spent_row = (end.tv_sec - start.tv_sec) * 1000.0 + (end.tv_nsec - start.tv_nsec) / 1e6;
            printf("Tiempo para sum_by_row con matriz %d x %d: %f milisegundos\n", N, M, time_spent_row);

            // Medir el tiempo de ejecución para recorrer por columnas
            clock_gettime(CLOCK_MONOTONIC, &start);
            sum = sum_by_column(matrix, N, M);
            clock_gettime(CLOCK_MONOTONIC, &end);
            double time_spent_column = (end.tv_sec - start.tv_sec) * 1000.0 + (end.tv_nsec - start.tv_nsec) / 1e6;
            printf("Tiempo para sum_by_column con matriz %d x %d: %f milisegundos\n", N, M, time_spent_column);

            // Escribir resultados en el archivo CSV
            fprintf(fp, "%d,%d,%f,%f\n", N, r + 1, time_spent_row, time_spent_column);

            // Liberar la memoria
            for (int i = 0; i < N; ++i) {
                free(matrix[i]);
            }
            free(matrix);
        }
    }

    fclose(fp);
    return 0;
}