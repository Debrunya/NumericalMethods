#include <cmath>
#include <vector>

#include <iostream>
using namespace std;


const double PI = 3.141592653589793;

vector<vector<double>> NonStatETC(int _N = 40, int _M = 100000, double _x_s = 0.0, double _x_f = 1.0, double _t_s = 0.0, double _t_f = 10.0)
{
//init vars
    double x_start, x_finish, time_start, time_finish;
    int N, M;
    double tau, h;
    vector<vector<double>> grid;

    x_start = _x_s;
    x_finish = _x_f;
    time_start = _t_s;
    time_finish = _t_f;
    N = _N + 1;
    M = _M + 1;

    h = (x_finish - x_start) / (N - 1);
    tau = (time_finish - time_start) / (M - 1);

//resize grid
    grid.resize(N);
    for (int i = 0; i < N; i++)
    {
        grid[i].resize(M);
    }

//solve Left Right Columns
    double tau_n = time_start;

    for (int i = 0; i < M; i++)
    {
        grid[0][i] = cos(tau_n);

        grid[N - 1][i] = sin(4.0 * tau_n);
        tau_n += tau;
    }

//solve Bottom Row
    double x_n = x_start;

    for (int i = 0; i < N; i++)
    {
        grid[i][0] = 1 - pow(x_n, 2);
        x_n += h;
    }

//solve Centre of grid
    x_n = x_start + h;
    tau_n = time_start;
    double gamma_sqr = 3.0;

    for (int j = 0; j < M - 1; j++)
    {
        for (int i = 1; i < N - 1; i++)
        {
            grid[i][j + 1] = grid[i][j] + (gamma_sqr * (grid[i - 1][j] - 2.0 * grid[i][j] + grid[i + 1][j]) / pow(h, 2)
                + tau_n * cos(PI * x_n) / (tau_n + 1.0)) * tau;
            x_n += h;
        }
        tau_n += tau;
    }

    return grid;
}