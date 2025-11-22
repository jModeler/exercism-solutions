#include "grains.h"
#include <math.h>

uint64_t square(uint8_t index) {
    if (index <= 0 || index > 64) {
        return 0;
    } else{
        double power = (double)index - 1;
        uint64_t grains = (uint64_t) pow(2.0, power);
        return grains; 
    }
}

uint64_t total(void) {
    uint64_t all_grains = 0;
    for(int i = 1; i <= 64; i++) {
        all_grains += square(i);
    }
    return all_grains;
}
