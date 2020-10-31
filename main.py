from calendar_funcions import *

if __name__ == '__main__':

    calendar = list(
        [tuple(list([1, 2])), tuple(list([0, 3])), tuple(list([2, 4])),
         tuple(list([6, 7])), tuple(list([7, 8])), tuple(list([9, 10]))])
    print(calendar)
    final_list = calendar_func(calendar)
    print(final_list)
