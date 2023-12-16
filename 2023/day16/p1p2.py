lines = open(0).read().splitlines()

class Beam:
    def __init__(self, i, j, di, dj):
        self.i = i
        self.j = j
        self.di = di
        self.dj = dj

allEdges = []
for i in range(len(lines)):
    allEdges.append(Beam(i, -1, 0, 1))
    allEdges.append(Beam(i, len(lines[0]), 0, -1))

for j in range(len(lines[0])):
    allEdges.append(Beam(-1, j, 1, 0))
    allEdges.append(Beam(len(lines), j, -1, 0))

p1, p2 = 0, 0
for startBeam in allEdges:
    beams = [startBeam]

    g = [[c for c in line] for line in lines]
    energized = [[False for _ in line] for line in lines]
    dirs = [[set() for _ in line] for line in lines]

    R, C = len(g), len(g[0])

    while len(beams) > 0:
        beam = beams.pop()

        while True:
            beam.i += beam.di
            beam.j += beam.dj
            if not (beam.i in range(R) and beam.j in range(C)) or (beam.di, beam.dj) in dirs[beam.i][beam.j]:
                break
            
            energized[beam.i][beam.j] = True
            dirs[beam.i][beam.j].add((beam.di, beam.dj))

            if g[beam.i][beam.j] == "/":
                if beam.di == 0:
                    beam.di = -beam.dj
                    beam.dj = 0
                else:
                    beam.dj = -beam.di
                    beam.di = 0
            elif g[beam.i][beam.j] == "\\":
                if beam.di == 0:
                    beam.di = beam.dj
                    beam.dj = 0
                else:
                    beam.dj = beam.di
                    beam.di = 0
            elif g[beam.i][beam.j] == "-":
                if beam.dj == 0:
                    beams.append(Beam(beam.i, beam.j, 0, 1))
                    beam.dj = -1
                    beam.di = 0
            elif g[beam.i][beam.j] == "|":
                if beam.di == 0:
                    beams.append(Beam(beam.i, beam.j, 1, 0))
                    beam.di = -1
                    beam.dj = 0

    energy = sum(sum(row) for row in energized)
    p1 = energy if p1 == 0 else p1
    p2 = max(p2, energy)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")