class Solution {
public:
    int fib(int N) {
        if (cache.count(N) > 0) {
            return cache.at(N);
        }
        else if (N == 1) {
            cache[N] = 1;
        } else if (N < 1) {
            cache[N] = 0;
        } else {
            cache[N] = fib(N - 2) + fib(N - 1);
        }

        return cache[N];
    }
private:
    map<int, int> cache;

};