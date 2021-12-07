#include "MyMethods.h"

const double PI = 3.141592653589793;

void NonStatETC::solveLeftCol()
{
    double tau_n = time_start;

    for (int i = 0; i < M; i++)
    {
        grid[0][i] = cos(tau_n);
        tau_n += tau;
    }

    return;
}


void NonStatETC::solveRightCol()
{
    double tau_n = time_start;

    for (int i = 0; i < M; i++)
    {
        grid[N - 1][i] = sin(4.0*tau_n);
        tau_n += tau;
    }

    return;
}


void NonStatETC::solveBottomRow()
{
    double x_n = x_start;

    for (int i = 0; i < N; i++)
    {
        grid[i][0] = 1-pow(x_n, 2);
        x_n += h;
    }

    return;
}


void NonStatETC::solveCenter()
{
    double x_n = x_start + h;
    double tau_n = time_start;
    double gamma_sqr = 3.0;

    for (int j = 0; j < M - 1; j++)
    {
        for (int i = 1; i < N - 1; i++)
        {
            grid[i][j + 1] = grid[i][j] + (gamma_sqr * cdo(i, j) + g(x_n, tau_n)) * tau;
            x_n += h;
        }
        tau_n += tau;
    }

    return;
}


double NonStatETC::cdo(int i, int j)
{
    return (grid[i - 1][j] - 2.0 * grid[i][j] + grid[i + 1][j]) / pow(h, 2);
}


double NonStatETC::g(double _x_n, double _tau_n)
{
    return _tau_n * cos(PI * _x_n) / (_tau_n + 1.0);
}


void NonStatETC::parameters()
{
    cout << endl << "Параметры метода" << endl
        << "x = [" << x_start << "," << x_finish << "], t = ["
        << time_start << "," << time_finish << "], N = " << N - 1 << ", M = " << M - 1 << endl << endl;
    return;
}


void NonStatETC::print()
{
    //cout.setf(ios::scientific);
    cout.setf(ios::left);

    for (int j = M - 1; j >= 0; j -= 500)
    {
        cout.width(6);
        cout << j << " ";
        for (int i = 0; i < N; i++)
        {
            cout.width(12);
            cout.precision(6);
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }

    return;
}

vector<vector<double>> NonStatETC::get_grid()
{
    return grid;
}
