#include <cstdio>
#include <cblas.h>
int main() {
	const int N = 3, M = 2, K = 5;
	double A[N][M] = {{2, -1},{1, 1},{2, 4}};
	double B[M][K] = {{1, 2, 3, 4, 5},{5, -3, 1, 10, 7}};
	double C[N][K]{};
	cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans,
			N, K, M, 1.0, &A[0][0],
			M, &B[0][0], K, 0.0,
			&C[0][0], K);
	for(int i = 0; i < 3; i++){
		for(int j = 0; j < 3; j++)
			printf("%f ", C[i][j]);
		printf("\n");
	}
	return 0;
}
