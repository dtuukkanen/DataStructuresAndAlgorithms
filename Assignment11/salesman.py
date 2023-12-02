def salesman(city_map):
    n = len(city_map)  # number of cities
    min_edge = calculate_min_edges(city_map)  # min edge cost for each city
    visited = [False] * n  # visited cities
    min_cost = [float("inf")]  # min cost initialization
    best_path = [0] * (n + 1)  # best path initialization

    # branch and bound algorithm
    def branch_and_bound(curr_path, curr_bound, curr_weight, level, visited):
        # Base case: if all cities are visited
        if level == n:
            # Calculate current cost
            curr_res = curr_weight + city_map[curr_path[level - 1]][curr_path[0]]

            # Update minimum cost and best path if current cost is better
            if curr_res < min_cost[0]:
                min_cost[0] = curr_res

                for i in range(n):
                    best_path[i] = curr_path[i]

                best_path[n] = curr_path[0]

            return

        # Try next cities to find better path
        for i in range(n):
            if city_map[curr_path[level - 1]][i] != 0 and not visited[i]:
                # Calculate temporary bound
                temp = curr_bound
                curr_weight += city_map[curr_path[level - 1]][i]

                # Adjust the bound for next city
                if level == 1:
                    curr_bound -= (min_edge[curr_path[level - 1]] + min_edge[i]) / 2
                else:
                    curr_bound -= (min_edge[curr_path[level - 1]] + min_edge[i]) / 2

                # Explore further if it is promising
                if curr_bound + curr_weight < min_cost[0]:
                    curr_path[level] = i
                    visited[i] = True
                    branch_and_bound(
                        curr_path, curr_bound, curr_weight, level + 1, visited
                    )

                # Backtrack: Remove last city from path and restore the bound
                curr_weight -= city_map[curr_path[level - 1]][i]
                curr_bound = temp
                visited[i] = False

    # Start from the first city
    visited[0] = True
    curr_path = [-1] * (n + 1)
    curr_path[0] = 0
    branch_and_bound(curr_path, sum(min_edge), 0, 1, visited)
    return best_path


def calculate_min_edges(city_map):
    # Calculate minimum edge cost for each city
    min_edge = []

    for row in city_map:
        min_val = float("inf")

        for val in row:
            if 0 < val < min_val:
                min_val = val

        min_edge.append(min_val)

    return min_edge


if __name__ == "__main__":
    cost = 0

    city_map = [
        #     0   1   2   3   4
        [0, 12, 19, 16, 29],  # 0
        [12, 0, 27, 25, 5],  # 1
        [19, 27, 0, 8, 4],  # 2
        [16, 25, 8, 0, 14],  # 3
        [29, 5, 4, 14, 0],  # 4
    ]

    path = salesman(city_map)
    for i in range(len(city_map)):
        cost += city_map[path[i]][path[i + 1]]

    print(path)  # [0, 1, 4, 2, 3, 0]
    print(cost)  # 45
