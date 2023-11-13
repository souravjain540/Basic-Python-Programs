def knapsack_recursive(weights: list[int], values: list[int], capacity: int, item_index: int):
    """Returns the best possible total value for the provided instance of the Knapsack Problem.

    Arguments:
    weights    --   the list of the weights of the items
    values     --   the list of the values of the items
    capacity   --   the maximum weight the knapsack can carry
    item_index --   the index of the current item
    """

    # Base Case
    if item_index == -1 or capacity == 0:return 0

    # Check value without carrying the current item
    dont_carry_value = knapsack_recursive(weights, values, capacity, item_index)

    # Current item weight is above capacity, return value without carrying
    if weights[item_index] > capacity:return dont_carry_value

    # Current item weight isn't above capacity
    carry_item_profit = values[item_index]
    carry_value = knapsack_recursive(weights, values, capacity - weights[item_index], item_index)

    # Return the larger between the value carrying the item and the value not carrying the item
    return max(carry_item_profit + carry_value, dont_carry_value)


if __name__ == "__main__":
    capacity = 8
    weights = [3, 2, 4]
    values = [6, 8, 7]
    item_count = len(weights)
    print(knapsack_recursive(weights, values, capacity, item_count - 1))