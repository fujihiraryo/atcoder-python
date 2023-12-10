#include <math.h>

#include <algorithm>
#include <iostream>

long solve(long a) {
    long l = 0;
    long r = std::pow(10l, 20l);
    while (r - l > 1) {
        long m = (l + r) / 2;
        if (std::pow(m, 2l) <= a) {
            l = m;
        } else {
            r = m;
        }
    }
    return l;
}

int main() {
    long d;
    std::cin >> d;
    long xmax = solve(d) + 1;
    long ans = std::pow(10l, 20l);
    for (long x = 0; x < xmax + 1; x++) {
        long y = solve(d - std::pow(x, 2l));
        long a1 = std::abs(std::pow(x, 2l) + std::pow(y, 2l) - d);
        if (a1 < ans) {
            ans = a1;
        }
        long a2 = std::abs(std::pow(x, 2l) + std::pow(y + 1, 2l) - d);
        if (a2 < ans) {
            ans = a2;
        }
    }
    std::cout << ans << std::endl;
}
