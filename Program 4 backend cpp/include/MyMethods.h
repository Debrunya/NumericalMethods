#include <iostream>
using namespace std;

#include <vector>
#include <cmath>


class NonStatETC //nonstationary equation of thermal conductivity grid
{
    double x_start, x_finish, time_start, time_finish;
    int N, M;
    double tau, h;
    vector<vector<double>> grid;

public:

NonStatETC(int _N = 40, int _M = 100000, double _x_s = 0.0, double _x_f = 1.0, double _t_s = 0.0, double _t_f = 10.0):
    x_start(_x_s), x_finish(_x_f), time_start(_t_s), time_finish(_t_f), N(_N + 1), M(_M + 1)
{
    h = (x_finish - x_start) / (N - 1);
    tau = (time_finish - time_start) /(M - 1);

    grid.resize(N);
    for (int i = 0; i < N; i++)
    {
        grid[i].resize(M);
    }

    return;
}
~NonStatETC() {}

double cdo(int i, int j);
double g(double _x_n, double _tau_n);

void solveLeftCol();
void solveRightCol();
void solveBottomRow();
void solveCenter();

void parameters();
void print();

vector<vector<double>> get_grid();
};
