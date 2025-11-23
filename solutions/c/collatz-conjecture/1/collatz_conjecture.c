#include "collatz_conjecture.h"

int steps(int start) {
    if (start <= 0) {
        return ERROR_VALUE;
    } else {
        int count = 0;
        int num = start;
        while (num != 1) {
            if (num % 2 != 0) {
                num = 3*num + 1;
            } else {
                num /= 2;
            }
            count += 1;
        }
        return count;
    }
}
