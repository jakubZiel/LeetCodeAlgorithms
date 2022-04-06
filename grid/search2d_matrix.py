from typing  import List

def search_2d_matrix(matrix : List[List[int]], value : int) -> bool:
    ROWS  = len(matrix)
    COLS = len(matrix[0])

    def binary_search(array : List[int], value : int):
        l, r = 0, COLS - 1

        while l <= r:
            mid = (l + r) // 2
            if array[mid] > value:
                r = mid - 1
            elif array[mid] < value:
                l = mid + 1
            else: 
                return True

        return False

    l_row, r_row = 0,  ROWS - 1

    while l_row <= r_row:
        mid_row = (r_row + l_row) // 2

        if value < matrix[mid_row][0]:
            r_row = mid_row - 1
        elif value > matrix[mid_row][COLS - 1]:
            l_row = mid_row + 1
        else:
            return binary_search(matrix[mid_row], value)

    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

print(search_2d_matrix(matrix,3))