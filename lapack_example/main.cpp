#include <cstdio>
#include <lapacke.h>
int main() {
	double A[3][3] = {{2, -1, 5},{1, 1, -3},{2, 4, 1}};
	double b[3][1] = {{10}, {-2}, {1}};
	lapack_int n = 3, lda = 3, ldb = 1, nrhs = 1, info;
	int ipiv[3];
	info = LAPACKE_dgesv(LAPACK_ROW_MAJOR, n, nrhs, *A, lda, ipiv, *b, ldb);
	for(int i = 0; i < 3; i++)
		printf("%f\n", b[i][0]);
	return 0;
}
