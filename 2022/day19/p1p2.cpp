#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;

struct Blueprint{
    int oreForOre;
    int oreForClay;
    int oreForObsidian;
    int clayForObsidian;
    int oreForGeode;
    int obsidianForGeode;
};

vector<Blueprint> blueprints;
void read(){
    string s;
    while (getline(cin, s)){
        int num;
        int oreForOre;
        int oreForClay;
        int oreForObsidian, clayForObsidian;
        int oreForGeode, obsidianForGeode;
        sscanf(s.c_str(), "Blueprint %d: Each ore robot costs %d ore. Each clay robot costs %d ore. Each obsidian robot costs %d ore and %d clay. Each geode robot costs %d ore and %d obsidian.", 
        &num, &oreForOre, &oreForClay, &oreForObsidian, &clayForObsidian, &oreForGeode, &obsidianForGeode);

        blueprints.push_back({oreForOre, oreForClay, oreForObsidian, clayForObsidian, oreForGeode, obsidianForGeode});
    }
}

inline ull getKey(int rore, int rclay, int robsidian, int rgeode, int ore, int clay, int obsidian, int geode, int minute){
    return (ull) rore * 1000000000000000000 + rclay * 10000000000000000 + robsidian * 100000000000000 + rgeode * 1000000000000 + ore * 1000000000 + clay * 10000000 + obsidian * 10000 + geode * 100 + minute;
}

int currIndex = 0;
int totalMinutes = 24;
int best = 0;

unordered_map<ull, int> cache;
int dfs(int rore, int rclay, int robsidian, int rgeode, int ore, int clay, int obsidian, int geode, int minute){
    ull key = getKey(rore, rclay, robsidian, rgeode, ore, clay, obsidian, geode, minute);
    if(cache.count(key)){
        return cache[key];
    }

    int minutesLeft = totalMinutes - minute;
    int guaranteedToEnd = geode + (minutesLeft * rgeode);
    int makeOneEveryTurn = (minutesLeft * (minutesLeft - 1) / 2);

    // If it is impossible to get a new maximum amount of geodes then prune this sequence
    if(guaranteedToEnd + makeOneEveryTurn < best){
        cache[key] = INT_MIN;
        return INT_MIN;
    }
    
    if(minute == totalMinutes){
        best = max(best, geode);
        return geode;
    }

    int ans = 0;

    // can afford geode robot
    if(ore >= blueprints[currIndex].oreForGeode && obsidian >= blueprints[currIndex].obsidianForGeode){
        int oreCost = blueprints[currIndex].oreForGeode;
        int obsidianCost = blueprints[currIndex].obsidianForGeode;
        ans = max(ans, dfs(rore, rclay, robsidian, rgeode + 1, 
            ore - oreCost + rore, clay + rclay, obsidian - obsidianCost + robsidian, geode+rgeode, minute+1));
        ans = max(ans, dfs(rore, rclay, robsidian, rgeode, ore + rore, clay + rclay, obsidian+robsidian, geode+rgeode, minute+1));

        // Always build geode robot if possible
        cache[key] = ans;
        return ans;
    }

    // can afford ore robot
    if(ore >= blueprints[currIndex].oreForOre){
        int oreCost = blueprints[currIndex].oreForOre;
        ans = max(ans, dfs(rore + 1, rclay, robsidian, rgeode, 
            ore - oreCost + rore, clay + rclay, obsidian+robsidian, geode+rgeode, minute+1));
    }

    // can afford clay robot
    if(ore >= blueprints[currIndex].oreForClay){
        int oreCost = blueprints[currIndex].oreForClay;
        ans = max(ans, dfs(rore, rclay + 1, robsidian, rgeode, 
            ore - oreCost + rore, clay + rclay, obsidian+robsidian, geode+rgeode, minute+1));
    }
    
    // can afford obsidian robot
    if(ore >= blueprints[currIndex].oreForObsidian && clay >= blueprints[currIndex].clayForObsidian){
        int oreCost = blueprints[currIndex].oreForObsidian;
        int clayCost = blueprints[currIndex].clayForObsidian;
        ans = max(ans, dfs(rore, rclay, robsidian + 1, rgeode, 
            ore - oreCost + rore, clay - clayCost + rclay, obsidian+robsidian, geode+rgeode, minute+1));
    }
    
    // dont buy any robot
    ans = max(ans, dfs(rore, rclay, robsidian, rgeode, ore + rore, clay + rclay, obsidian+robsidian, geode+rgeode, minute+1));
    cache[key] = ans;
    return ans;
}

void doPart(int part){
    int ans = (part == 1 ? 0 : 1);
    int bsize = (int) blueprints.size();
    int maxIndex = (part == 1 ? bsize : min(3, bsize));
    totalMinutes = (part == 1 ? 24 : 32);

    for(currIndex = 0; currIndex < maxIndex; currIndex++){
        int blueprintVal = dfs(1, 0, 0, 0, 0, 0, 0, 0, 0);
        cache.clear();
        best = 0;
        if(part == 1){
            ans += (blueprintVal * (currIndex + 1));
        } else{
            ans *= blueprintVal;
        }
        cout << "Blueprint " << (currIndex + 1) << ": " << blueprintVal << endl;
    }

    cout << "Part " << part << ": " << ans << endl;
}

int main(){
    read();
    doPart(1);
    doPart(2);

    return 0;
}