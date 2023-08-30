#!/usr/bin/python3
""" Island Perimeter mandatory """


def test0(n):
    """
    @n: number of the grid
    Returns: 0 if n is 1 or 1 if n is 0
    """
    if (n == 0):
        return 1
    return 0


def island_perimeter(grid):
    """"
    @grid: is a list of list of integers:
                *** 0 represents water
                *** 1 represents land
                *** Each cell is square, with a side
                    length of 1
                *** Cells are connected horizontally/vertically
                    (not diagonally).
                *** grid is rectangular, with its width and
                    height not exceeding 100
            The grid is completely surrounded by water
            There is only one island (or nothing).
            The island doesn’t have “lakes” (water inside that isn’t
                connected to the water surrounding the island).
    """
    row = len(grid)
    col = len(grid[0])
    assert (1 <= row and col <= 100), "length must be between 1 an 100"

    y = 0
    for i in range(row):
        for j in range(col):
            assert (grid[i][j] == 0) or (grid[i][j] == 1),\
                                        "grind application"
            if grid[i][j] == 1:
                if i-1 < 0:
                    y += 1
                else:
                    y += test0(grid[i-1][j])
                if j-1 < 0:
                    y += 1
                else:
                    y += test0(grid[i][j-1])

                try:
                    y += test0(grid[i+1][j])
                except IndexError:
                    y += 1
                try:
                    y += test0(grid[i][j+1])
                except IndexError:
                    y += 1

    return y
