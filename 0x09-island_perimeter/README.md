# Island Perimeter

This repository contains a Python script `0-island_perimeter.py` that implements a function `island_perimeter(grid)` to calculate the perimeter of an island described within a grid.

## Function Description

The function `island_perimeter(grid)` takes in a grid, which is a list of lists of integers. It computes and returns the perimeter of the island represented in the grid according to the following specifications:

- The grid consists of:
  - 0, representing water
  - 1, representing land
- Each cell in the grid is a square with a side length of 1.
- Cells are connected horizontally or vertically but not diagonally.
- The grid is rectangular, with its width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is only one island or nothing (an empty grid).
- The island doesn’t contain "lakes" (water inside that isn’t connected to the water surrounding the island).
