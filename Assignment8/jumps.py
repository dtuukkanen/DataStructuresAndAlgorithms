def jumps(n, a, b):
    jumps = [0] * (n+1)
    jumps_dynamic(n, a, b, jumps)
    return jumps[n]


def jumps_dynamic(n, a, b, jumps):
    for i in range(n+1):
        if i == 0:
            jumps[i] = 1
        elif i < 0:
            jumps[i] = 0
        else:
            jumps[i] = jumps[i-a] + jumps[i-b]


if __name__ == "__main__":
    print(jumps(4, 1, 2))  # 5
    print(jumps(8, 2, 3))  # 4
    print(jumps(11, 6, 7))  # 0
    print(jumps(30, 3, 5))  # 58
    print(jumps(100, 4, 5))  # 1167937
