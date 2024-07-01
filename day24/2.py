from sympy import Symbol, solve_poly_system

with open("in.txt") as file:
    lines = file.readlines()

stones = []
for line in lines[:3]:
    pos, vel = line.split("@")
    pos = [int(a) for a in pos.strip().split(", ")]
    vel = [int(a) for a in vel.strip().split(", ")]
    stones.append((pos, vel))


a, b, c = Symbol("a"), Symbol("b"), Symbol("c")
va, vb, vc = Symbol("va"), Symbol("vb"), Symbol("vc")
variables = [a, b, c, va, vb, vc]
equations = []
for idx, (pos, vel) in enumerate(stones):
    x, y, z = pos
    vx, vy, vz = vel
    t = Symbol("t" + str(idx))
    variables.append(t)
    equations.append(x + t*vx - a + t*va)
    equations.append(y + t*vy - b + t*vb)
    equations.append(z + t*vz - c + t*vc)

res = solve_poly_system(equations, variables)
print(res)
print(sum(res[0][:3]))




