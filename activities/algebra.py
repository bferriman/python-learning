# only addition
# get x first
# solve_eq("x + 4 = 9")

def solve_eq(eq):
    eq_stripped = eq.strip()
    eq_list = eq_stripped.split()
    num_1, num_2 = int(eq_list[2]), int(eq_list[4])
    print("x =", str(num_2 - num_1))


solve_eq("x + 4 = 9")
