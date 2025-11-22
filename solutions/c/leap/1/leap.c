#include "leap.h"

bool leap_year(int year) {
    int div_4 = year%4;
    int div_100 = year%100;
    int div_400 = year%400;
    if (div_4 != 0) {
        return false;
    } else if (div_100 == 0 && div_400 != 0) {
        return false;
    } else {
        return true;
    }
}
