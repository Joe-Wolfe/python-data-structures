
def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    sum = 0
    length = len(matrix)
    for position in range(length):
        # hits the topleft > bottomright diagnol
        sum += matrix[position][position]
        # hits the bottomleft to topright diagnol
        sum += matrix[length-position-1][position]
    return sum
