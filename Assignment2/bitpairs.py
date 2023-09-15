def pairs(s):
    distance = 0
    amount_of_ones = 0
    sum = 0

    for i in s:
        if i == "1":
            amount_of_ones += 1
            sum += distance
        distance += amount_of_ones

    return sum


if __name__ == "__main__":
    print(pairs("100101"))          # 10
    print(pairs("101"))             # 2
    print(pairs("100100111001"))    # 71
