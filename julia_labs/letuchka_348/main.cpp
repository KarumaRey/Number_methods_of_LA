#include <iostream>
#include <vector>
#include <random>
#include <math.h>

using namespace std;

vector<vector<double>> generateArray(int n) {
    vector<vector<double>> A(n, vector<double>(n, 0));
    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<double> dis(1, 20);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            A[i][j] = dis(gen);
        }
    }

    return A;
}

void LU_decomp(vector<vector<double>> A, vector<vector<double>>& L, vector<vector<double>>& U) {
    int n = A.size();
    for (int i = 0; i < n; i++) {
        
        for (int k = i; k < n; k++) {
            
            double sum = 0;
            for (int j = 0; j < i; j++)
                sum += L[i][j] * U[j][k];
            U[i][k] = A[i][k] - sum;
        }
        for (int k = i; k < n; k++) {
            
            if (i == k)
                L[i][i] = 1;
            else {
                double sum = 0;
                for (int j = 0; j < i; j++)
                    sum += L[k][j] * U[j][i];
                L[k][i] = (A[k][i] - sum) / U[i][i];
                
            }
        }
        
    }
}



int main() {
    // vector<vector<double>> 
    // A = {{1, 2, 3},
    //  {4, 5, 6}, 
    //  {7, 8, 9}};
    // int n = A.size();

    int n = 5;

    vector<vector<double>> A = generateArray(n);


    cout << "Матрица A:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << A[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;

    vector<vector<double>> L(n, vector<double>(n, 0));
    vector<vector<double>> U(n, vector<double>(n, 0));
    LU_decomp(A, L, U);

    cout << "Матрица L:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << L[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;

    cout << "Матрица U:" << endl;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << U[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;


    vector<vector<double>> A_check(n, vector<double>(n, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            double sum = 0;
            for (int k = 0; k < n; k++) {
                sum += L[i][k] * U[k][j];
            }
            A_check[i][j] = sum;
        }
    }

    cout << "Проверка LU-разложения:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << A_check[i][j] << " ";
        }
        cout << endl;
    }


    return 0;
}