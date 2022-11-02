def find_max_and_index(list_of_nums):
    max_value = 0
    index = 0
    for idx, num in enumerate(list_of_nums):
        if num > max_value:
            max_value = num
            index = idx

    print(f"Max number is {max_value} with an index of: {index}")



find_max_and_index([3,4,6,10, 22, 5, 18])