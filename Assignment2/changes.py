def changes(A):
    changes = 0
    for i in range(len(A) - 1):
        if A[i] == A[i+1]:
            changes += 1
            A[i+1] = 0
    return changes


if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))     # 2
    print(changes([1, 2, 3, 4, 5]))     # 0
    print(changes([1, 1, 1, 1, 1]))     # 2
