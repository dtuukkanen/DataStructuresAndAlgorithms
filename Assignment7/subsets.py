def subsets(n: int) -> list:
    # Save all subsets in a list
    subsets = []

    # Loop through all possible subsets
    for i in range(1, 2**n):
        # Save subset in a list
        subset = []

        # Loop through all bits in i
        for j in range(n):
            # If bit is 1, add j+1 to subset
            if i & (1 << j):
                subset.append(j+1)

        # Add subset to list of subsets
        subsets.append(subset)

    # Return list of subsets
    return subsets


if __name__ == "__main__":
    print(subsets(1))   # [[1]]
    print(subsets(2))   # [[1], [2], [1, 2]]
    print(subsets(3))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print(subsets(4))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3],
    #  [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4],
    #  [2, 3, 4], [1, 2, 3, 4]]
    S = subsets(10)
    print(S[95])    # [6, 7]
    print(S[254])   # [1, 2, 3, 4, 5, 6, 7, 8]
    print(S[826])   # [1, 2, 4, 5, 6, 9, 10]
