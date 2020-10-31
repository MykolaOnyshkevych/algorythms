from random import shuffle


def partition(my_array, start, end):
    pivot = my_array[start][0]
    low = start + 1
    high = end

    while True:

        while low <= high and my_array[high][0] > pivot:

            high = high - 1

        while low <= high and not my_array[low][0] > pivot:

            low = low + 1

        if low <= high:
            my_array[low], my_array[high] = my_array[high], my_array[low]

        else:
            break
    my_array[start], my_array[high] = my_array[high], my_array[start]

    return high



def quick_sort(given_array, start, end):
    if start >= end:
        return

    sort_partition = partition(given_array, start, end)

    quick_sort(given_array, start, sort_partition - 1)
    quick_sort(given_array, sort_partition + 1, end)


def sort(given_array):

    shuffle(given_array)
    quick_sort(given_array, 0, len(given_array) - 1)



def calendar_func(new_calendar):
    """
    >>> my_calendar = list([tuple(list([1, 2])), tuple(list([0, 3])), tuple(list([2, 4])),tuple(list([6, 7])), tuple(list([7, 8])), tuple(list([9, 10]))])
    >>> calendar_func(my_calendar)
    [(0, 4), (6, 8), (9, 10)]
    """
    sort(new_calendar)

    resault = list()

    start_working, finish_working = new_calendar[0]

    for iterator in range(0, len(new_calendar)):
        if iterator < len(new_calendar) - 1:
            item_next = new_calendar[iterator + 1]
        if iterator >= len(new_calendar) - 1:
            resault.append((start_working, new_calendar[iterator][1]))
            break
        if finish_working >= item_next[0] and finish_working >= item_next[1]:

            finish_working = new_calendar[iterator][1]

        elif item_next[1] >= finish_working >= item_next[0]:

            finish_working = item_next[1]

        else:
            resault.append((start_working, finish_working))
            start_working, finish_working = item_next

    return resault


def main():
    import doctest

    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()