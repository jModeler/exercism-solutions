#include "darts.h"
#include <stdint.h>
#include <math.h>

uint8_t score(coordinate_t landing_position) {
    float x_sq = pow(landing_position.x, 2.0);
    float y_sq = pow(landing_position.y, 2.0);
    float distance = pow(x_sq + y_sq, 0.5);
    if (distance <= 1.0) {
        return 10;
    } else if (distance <= 5.0) {
        return 5;
    } else if (distance <= 10.0) {
        return 1;
    } else {
        return 0;
    }
}
