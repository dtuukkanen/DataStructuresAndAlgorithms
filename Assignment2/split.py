def split(T):
    array_size = len(T)

    # Calculate the maximum on the left side
    left_max = [0] * array_size
    current_max = 0
    for i in range(array_size):
        current_max = max(current_max, T[i])
        left_max[i] = current_max

    # Calculate the minimum on the right side
    right_min = float("inf")
    counter = 0
    for i in range(array_size - 1, 0, -1):
        right_min = min(right_min, T[i])
        if left_max[i - 1] < right_min:
            counter += 1

    return counter


if __name__ == "__main__":
    print(split([1, 2, 3, 4, 5]))  # 4
    print(split([5, 4, 3, 2, 1]))  # 0
    print(split([2, 1, 2, 5, 7, 6, 9]))  # 3
    print(split([1, 2, 3, 1]))  # 0
