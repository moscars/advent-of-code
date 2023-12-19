r, v = open(0).read().split("\n\n")
r = r.splitlines()
v = v.splitlines()

rules = {}
for rule in r:
    rule, rest = rule[:-1].split("{")
    rules[rule] = rest.split(",")

values = []
for val in v:
    mp = {}
    parts = val[1:-1].split(",")
    for part in parts:
        mp[part[0]] = int(part[2:])
    values.append(mp)

accepted = []
for mp in values:
    curr = "in"
    while True:
        if curr == "A":
            accepted.append(mp)
            break
        elif curr == "R":
            break
        
        for rule in rules[curr]:
            if not ":" in rule:
                curr = rule
                break
            else:
                s, target = rule.split(":")
                key, comp, num = s[0], s[1], int(s[2:])

                if comp == "<":
                    if mp[key] < num:
                        curr = target
                        break
                elif comp == ">":
                    if mp[key] > num:
                        curr = target
                        break

print(f"Part 1: {sum(sum(x.values()) for x in accepted)}")