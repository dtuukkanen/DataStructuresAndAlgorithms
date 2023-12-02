# This implementation is based on First-Fit-Decreasing (FFD) algorithm
def binpack(items, S):
    # Sort items in decreasing order
    items.sort(reverse=True)

    # Initialize bins
    bins = [[]]

    # Iterate over each item
    for item in items:
        # Try to place item in a bin
        placed = False
        for bin in bins:
            if sum(bin) + item <= S:
                bin.append(item)
                placed = True
                break

        # If item could not be placed, create a new bin
        if not placed:
            bins.append([item])

    return bins


if __name__ == "__main__":
    items = [9, 3, 3, 6, 10, 4, 6, 8, 6, 3]
    B = 10

    bins = binpack(items, B)

    for i in range(len(bins)):
        print(f"bin {i+1}: {bins[i]}")

# A possible output:
#   bin 1: [9]
#   bin 2: [3, 3, 4]
#   bin 3: [6, 3]
#   bin 4: [10]
#   bin 5: [6]
#   bin 6: [8]
#   bin 7: [6]
