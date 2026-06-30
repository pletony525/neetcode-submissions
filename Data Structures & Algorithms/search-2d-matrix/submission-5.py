class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix) - 1
        l = 0
        while l <= r:
            p = l + ((r-l) // 2)
            row_r = len(matrix[0]) - 1
            row_l = 0
            if target > matrix[p][row_r]:
                l = p + 1
            elif target < matrix[p][row_l]:
                r = p - 1
            else:
                while row_l <= row_r:
                    row_p = row_l + ((row_r - row_l) // 2)
                    if target > matrix[p][row_p]:
                        row_l = row_p + 1
                    elif target < matrix[p][row_p]:
                        row_r = row_p - 1
                    else:
                        return True
                return False

        return False