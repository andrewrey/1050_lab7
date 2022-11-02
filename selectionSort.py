


def sort():
    userNumberList = []

    stop_flag = False

    while not stop_flag:
        entered_number = input('Enter a number or type "S" to stop: ')
        if entered_number == "S" or entered_number == "s":
            stop_flag = True
        else: 
            userNumberList.append(int(entered_number))

    userSortChoice = input('Push B for bubble sort or S for selection sort: ').lower()

    if userSortChoice == "b":
        swap_flag = True
        print(f"Your original list: {userNumberList}")
        while swap_flag:
            swap_flag = False
            for x in range(len(userNumberList) - 1):
                if userNumberList[x] < userNumberList[x + 1]:
                    temp = userNumberList[x]
                    userNumberList[x] = userNumberList[x + 1]
                    userNumberList[x + 1] = temp
                    swap_flag = True
        print(f"Your bubble sorted list in descending order: {userNumberList}")

    elif userSortChoice == "s":
        idx_length = range(0,len(userNumberList) - 1)

        print(f"Your original list: {userNumberList}")
        
        for x in idx_length:
            max_value = x

            for y in range(x + 1, len(userNumberList)):
                if userNumberList[y] > userNumberList[max_value]:
                    max_value = y

            if max_value != x:
                userNumberList[max_value], userNumberList[x] = userNumberList[x], userNumberList[max_value]
        print(f"Your selection sorted list in descending order: {userNumberList}")

sort()


