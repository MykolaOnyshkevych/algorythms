import time
import csv


class MechanicPuzzle:
    selection_comparisons_counter = 0
    selection_swap_counter = 0
    merge_comparisons_counter = 0
    merge_swap_counter = 0

    def __init__(self, puzzle_matherial: str, puzzle_type: str, elements_quantity: int, garanty_in_monthes: int):
        self.puzzle_matherial = puzzle_matherial
        self.puzzle_type = puzzle_type
        self.elements_quantity = elements_quantity
        self.garanty_in_monthes = garanty_in_monthes

    def __str__(self):
        return "Puzzle Matherial:"+self.puzzle_matherial+"   Puzzle Type:"+self.puzzle_type+"   Elements Quantity:"\
               +str(self.elements_quantity)+"   Garanty In Monthes:"+str(self.garanty_in_monthes)

    def merge_sort_garanty_in_monthes(puzzles:list):
        if len(puzzles) > 1:
            middle = len(puzzles) // 2
            left_arr = puzzles[:middle]
            right_arr = puzzles[middle:]

            left_arr = MechanicPuzzle.merge_sort_garanty_in_monthes(left_arr)
            right_arr = MechanicPuzzle.merge_sort_garanty_in_monthes(right_arr)

            left_iterator = right_iterator = general_iterator = 0

            while left_iterator < len(left_arr) and right_iterator < len(right_arr):
                MechanicPuzzle.merge_comparisons_counter += 1
                if left_arr[left_iterator].garanty_in_monthes > right_arr[right_iterator].garanty_in_monthes:
                    puzzles[general_iterator] = left_arr[left_iterator]
                    left_iterator += 1
                else:
                    puzzles[general_iterator] = right_arr[right_iterator]
                    right_iterator += 1
                general_iterator += 1
                MechanicPuzzle.merge_swap_counter += 1

            while left_iterator < len(left_arr):
                puzzles[general_iterator] = left_arr[left_iterator]
                MechanicPuzzle.merge_comparisons_counter += 1
                MechanicPuzzle.merge_swap_counter += 1
                left_iterator += 1
                general_iterator += 1

            while right_iterator < len(right_arr):
                puzzles[general_iterator] = right_arr[right_iterator]
                MechanicPuzzle.merge_comparisons_counter += 1
                MechanicPuzzle.merge_swap_counter += 1
                right_iterator += 1
                general_iterator += 1

        return puzzles

    def selection_sort_elements_quantity(puzzles:list):
        list_length = len(puzzles)
        for i in range(list_length - 1):
            max_index = i
            for j in range(i + 1, list_length):

                if puzzles[max_index].elements_quantity < puzzles[j].elements_quantity:
                    max_index = j
                MechanicPuzzle.selection_comparisons_counter += 1
            if max_index != i:
                puzzles[i], puzzles[max_index] = puzzles[max_index], puzzles[i]
                MechanicPuzzle.selection_swap_counter += 1

        return puzzles


def open_file_csv(filename: str):
    puzzles = []
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for line in reader:
            puzzles.append(MechanicPuzzle(line[0], (line[1]), int(line[2]), int(line[3])))

    return puzzles



def main():
    puzzles = open_file_csv("puzlzes.csv")
    print("Selection Unsorted Array:")
    [print(puzzle) for puzzle in puzzles]
    print()

    print('Select sort desc')
    start = time.time()
    puzzles = MechanicPuzzle.selection_sort_elements_quantity(puzzles)
    end = time.time() - start
    print("Working time: " + str(end))
    print("Comparisons: " + str(MechanicPuzzle.selection_comparisons_counter))
    print("Swaps: " + str(MechanicPuzzle.selection_swap_counter))
    print()
    print("Selection Sorted Array:")
    [print(puzzle) for puzzle in puzzles]

    print()

    print("Merge-sort Unsorted Array:")
    [print(puzzle) for puzzle in puzzles]
    print()
    print("Merge sort desc")
    start = time.time()
    puzzles = MechanicPuzzle.merge_sort_garanty_in_monthes(puzzles)
    end = time.time() - start
    print("Working time: " + str(end))
    print("Comparisons: " + str(MechanicPuzzle.merge_comparisons_counter))
    print("Swaps: " + str(MechanicPuzzle.merge_swap_counter))
    print()

    print("Merge-sort Sorted Array:")
    [print(puzzle) for puzzle in puzzles]


if __name__ == "__main__":
    main()


