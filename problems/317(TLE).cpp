#include <queue>
#include <vector>
#include <cmath>
#include <iostream>

using namespace std;


struct Index {
    int i;
    int j;
    int distance;
};


class Solution {
public:
    bool ValidCell(int i, int j, vector<vector<int>>& reached_by_buildings, vector<vector<int>>& grid, int current_building) {
        // check that {i, j} is inner of the grid and cell is reachable by all buildings checked previously
        if (i >= 0 && i < N && j >= 0 && j < M && reached_by_buildings[i][j] == (current_building - 1) && grid[i][j] == 0) {
            return true;
        }
        return false;
    }

    void BFS(int i, int j, vector<vector<int>>& grid, vector<vector<int>>& dis, vector<vector<int>>& reached_by_buildings, int current_building) {
        queue<Index> q;
        q.push({i, j, 0});

        while (!q.empty()) {
            Index node = q.front(); q.pop();
            int i = node.i; int j = node.j;
            if (node.distance != 0 && reached_by_buildings[i][j] == current_building - 1) { // reach by previous checked buildings
                dis[i][j] += node.distance;
                reached_by_buildings[i][j]++;
            }

            if (ValidCell(i + 1, j, reached_by_buildings, grid, current_building)) {
                q.push({i + 1, j, node.distance + 1});
            }
            if (ValidCell(i, j + 1, reached_by_buildings, grid, current_building)) {
                q.push({i, j + 1, node.distance + 1});
            }
            if (ValidCell(i - 1, j, reached_by_buildings, grid, current_building)) {
                q.push({i - 1, j, node.distance + 1});
            }
            if (ValidCell(i, j - 1, reached_by_buildings, grid, current_building)) {
                q.push({i, j - 1, node.distance + 1});
            }
        }
    }

    int shortestDistance(vector<vector<int>>& grid) {
        if (grid.size() == 0 || grid[0].size() == 0) {
            return -1;
        }
        this->N = grid.size(); this->M = grid[0].size();
        int number_of_buildings = 0;
        vector<vector<int>> dis(N, vector<int>(M, 0));
        vector<vector<int>> reached_by_buildings(N, vector<int>(M, 0));
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (grid[i][j] == 1) {
                    number_of_buildings++;
                    BFS(i, j, grid, dis, reached_by_buildings, number_of_buildings);
                }
            }
        }

        int MAX_INT = pow(2, 31) - 1;
        int min_sum = MAX_INT;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (reached_by_buildings[i][j] == number_of_buildings && dis[i][j] < min_sum) {
                    min_sum = dis[i][j];
                }
            }
        }

        return min_sum != MAX_INT ? min_sum : -1;
    }

private:
    int M, N;
};