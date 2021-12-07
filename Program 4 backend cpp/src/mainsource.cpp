#include "mainsource.h"


void mainsource()
{
    NonStatETC sol = NonStatETC(40, 100000);
    sol.parameters();
    sol.solveBottomRow();
    sol.solveLeftCol();
    sol.solveRightCol();
    sol.solveCenter();
    sol.print();

    return;
}
