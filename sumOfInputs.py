def sum_5_numbers():
    number_to_sum = []
    sum = 0
    for x in range(5):
        number_to_sum.append(int(input(f"Enter number {x+1}: ")))
    for num in number_to_sum:
        sum += num
    print(sum)


sum_5_numbers()