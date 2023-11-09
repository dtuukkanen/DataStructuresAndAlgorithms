def sums(items):
    total = sum(items)
    has_sum = [False] * (total + 1)
    # In case list contains only one item it has only one possible sum
    has_sum[1] = True

    # For each item in the list, check if the sum of the item and the previous
    # sums can be made. If so, set the corresponding index in has_sum to True.
    for item in items:
        for j in range(total, item - 1, -1):
            if has_sum[j - item]:
                has_sum[j] = True

    return count_sums(has_sum)


def count_sums(has_sum):
    count = 0
    for sum in has_sum:
        if sum:
            count += 1
    return count


if __name__ == "__main__":
    print(sums([1, 2, 3]))                  # 6
    print(sums([2, 2, 3]))                  # 5
    print(sums([1, 3, 5, 1, 3, 5]))         # 18
    print(sums([1, 15, 5, 23, 100, 55, 2]))  # 121
