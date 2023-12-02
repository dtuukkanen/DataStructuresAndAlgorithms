def sales(cars, customers):
    # Sort lists so that customers that have least amount of money can buy the cheapest car possible
    cars.sort()
    customers.sort()
    cars_sold = 0
    i = 0
    j = 0
    while i < len(cars) and j < len(customers):
        if cars[i] <= customers[j]:
            cars_sold += 1
            i += 1
            j += 1
        else:
            j += 1
    return cars_sold


if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))  # 3
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))  # 4
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))  # 3
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))  # 5
