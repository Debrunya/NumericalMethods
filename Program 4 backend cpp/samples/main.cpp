#include "mainsource.h"


int main()
{
    setlocale(LC_ALL, "Russian");

    while (true)
    {
        system("cls");

        while (true)
        {
            system("cls");

            bool err_flag = false;
            try
            {
                mainsource();
            }
            catch (exception& err)
            {
                err_flag = true;
                cout << endl << endl << endl
                    << "Выполнено исключение!!!" << endl << "Ошибка: " << err.what() << endl
                    << "Выйти - Esc, Перезапустить - Enter" << endl;
                int button = _getch(); //esc = 27, enter = 13, y = 127, n = 110
                if (button != 13)
                {
                    break;
                }
            }

            if (err_flag == false)
            {
                break;
            }
        }

        cout << endl << endl << endl
            << "Программа отработала!" << endl
            << "Выйти - Esc, Перезапустить программу - Enter" << endl;
        int button = _getch();
        if (button != 13)
        {
            break;
        }
    }

    return 0;
}
