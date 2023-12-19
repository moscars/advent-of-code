from copy import deepcopy

r, _ = open(0).read().split("\n\n")
r = r.splitlines()

rules = {}
for rule in r:
    rule, rest = rule[:-1].split("{")
    rules[rule] = rest.split(",")
    
ans = 0
def dfs(wf, sm, la):
    if wf == "A":
        global ans
        possibilities = 1
        for i in range(4):
            possibilities *= (la[i] - sm[i] + 1)
        ans += possibilities
        return
    elif wf == "R":
        return
    
    for rule in rules[wf]:
        if not ":" in rule:
            dfs(rule, sm, la)
        else:
            s, target = rule.split(":")
            key, comp, num = s[0], s[1], int(s[2:])
            idx = "xmas".index(key)

            if comp == "<":
                if sm[idx] < num:
                    nla = deepcopy(la)
                    nla[idx] = min(nla[idx], num - 1)
                    if sm[idx] <= nla[idx]:
                        dfs(target, deepcopy(sm), nla)
                        sm[idx] = num
            elif comp == ">":
                if la[idx] > num:
                    nsm = deepcopy(sm)
                    nsm[idx] = max(sm[idx], num + 1)
                    if nsm[idx] <= la[idx]:
                        dfs(target, nsm, deepcopy(la))
                        la[idx] = num

dfs("in", [1, 1, 1, 1], [4000, 4000, 4000, 4000])
print(f"Part 2: {ans}")