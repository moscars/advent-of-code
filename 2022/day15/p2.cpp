#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

int largest = 4000000;

int mannhattan(int x1, int y1, int x2, int y2){
    return abs(x1 - x2) + abs(y1 - y2);
}

vector<vector<int>> getClose(){
    vector<vector<int>> close;
    string s;
    while (getline(cin, s)){
        int sx, sy, bx, by;
        sscanf(s.c_str(), "Sensor at x=%d, y=%d: closest beacon is at x=%d, y=%d", &sx, &sy, &bx, &by);
        close.push_back({sx, sy, bx, by});
    }
    return close;
}

unordered_map<int, vector<pair<int, int>>> getCoveredRegions(vector<vector<int>> & close){
    unordered_map<int, vector<pair<int, int>>> coveredRegions;

    for (auto & c : close){
        int sx = c[0];
        int sy = c[1];
        int bx = c[2];
        int by = c[3];

        int beaconDist = mannhattan(sx, sy, bx, by);
        for (int y = max(sy - beaconDist - 1, 0); y <= min(sy + beaconDist + 1, largest); y++){
            int start = INT_MAX;
            int end = INT_MIN;
            int lo = 0;
            int hi = sx;
            while (lo <= hi){
                int mid = (lo + hi) / 2;
                if (mannhattan(sx, sy, mid, y) <= beaconDist){
                    start = min(start, mid);
                    hi = mid - 1;
                } else {
                    lo = mid + 1;
                }
            }

            lo = sx;
            hi = largest;
            while (lo <= hi){
                int mid = (lo + hi) / 2;
                if (mannhattan(sx, sy, mid, y) <= beaconDist){
                    end = max(end, mid);
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
            if (start != INT_MAX){
                coveredRegions[y].push_back({start, end});
            }
        }
    }
    return coveredRegions;
}

int main(){
    vector<vector<int>> close = getClose();
    unordered_map<int, vector<pair<int, int>>> coveredRegions = getCoveredRegions(close);
    
    for (int y = 0; y <= largest; y++){
        sort(coveredRegions[y].begin(), coveredRegions[y].end());
        int prevEnd = 0;
        for (auto & [startx, endx] : coveredRegions[y]){
            if (startx > prevEnd + 1){
                cout << (long long) (startx - 1) * 4000000 + y << endl;
                return 0;
            }
            prevEnd = max(endx, prevEnd);
        }
    }
}