#include <iostream>
#include <set>
#include <vector>
int main() {
    int n, q;
    std::cin >> n >> q;
    std::vector<std::set<int>> box(n);
    for (int i = 0; i < n; i++) {
        int c;
        std::cin >> c;
        box[i].insert(c);
    }
    for (int i = 0; i < q; i++) {
        int a, b;
        std::cin >> a >> b;
        if (box[a - 1].size() < box[b - 1].size()) {
            box[b - 1].merge(box[a - 1]);
            box[a - 1].clear();
        } else {
            box[a - 1].merge(box[b - 1]);
            box[b - 1].clear();
            std::swap(box[a - 1], box[b - 1]);
        }
        std::cout << box[b - 1].size() << std::endl;
    }
}
