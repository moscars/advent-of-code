#include <bits/stdc++.h>
using namespace std;

// runs in about 3 minutes.

int best = 0;
int64_t states = 0;
vector<string> graph;
vector<vector<bool>> seen;
vector<pair<int, int>> diffs = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
int R, C;
int gi, gj;

template <bool PART1>
void backtrack(int i, int j, int steps){
    if (i == gi && j == gj){
        best = max(best, steps);
        return;
    }
    
    states++;
    if (states % 1000000 == 0)
        cout << (states / 1000000) << " million states. Best found: " << best << endl;

    for (auto & [di, dj] : diffs){
        int ni = i + di, nj = j + dj;
        if (0 <= ni && ni < R && 0 <= nj && nj < C && graph[ni][nj] != '#' && !seen[ni][nj]){
            if constexpr (PART1){
                if (graph[ni][nj] == '>' && nj != j + 1)
                    continue;
                if (graph[ni][nj] == 'v' && ni != i + 1)
                    continue;
            }

            seen[i][j] = true;
            backtrack<PART1>(ni, nj, steps + 1);
            seen[i][j] = false;
        }
    }
}

int main(){
    string line;
    while (getline(cin, line))
        graph.push_back(line);

    R = graph.size(), C = graph[0].size();
    
    int si = 0;
    int sj = find(graph[0].begin(), graph[0].end(), '.') - graph[0].begin();
    gi = R - 1;
    gj = find(graph[R-1].begin(), graph[R-1].end(), '.') - graph[R-1].begin();


    seen = vector<vector<bool>>(R, vector<bool>(C, false));
    backtrack<true>(si, sj, 0);
    int p1 = best;
    
    states = 0;
    seen = vector<vector<bool>>(R, vector<bool>(C, false));
    backtrack<false>(si, sj, 0);
    
    cout << endl;
    cout << "Part 1: " << p1 << endl;
    cout << "Part 2: " << best << endl;
    return 0;
}