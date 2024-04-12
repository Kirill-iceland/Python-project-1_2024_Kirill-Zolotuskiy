import random

from src.maze.Maze import Maze
from src.algorithms.UnionFind import UnionFind

class SpanningTree:
    def get_index(x: int, y: int, width: int) -> int:
        return x * width + y

    def generate(width: int, height: int) -> Maze:
        maze = Maze(width, height, 0b1111)
        edges = []

        for i in range(height):

            for j in range(width):
                if (j + 1 < width):
                    edges.append((i, j, i, j + 1, 0))
                if (j > 0):
                    edges.append((i, j, i, j - 1, 1))
                if (i + 1 < height):
                    edges.append((i, j, i + 1, j, 2))
                if (i > 0):
                    edges.append((i, j, i - 1, j, 3))

        random.shuffle(edges)
        union_find = UnionFind(width * height)
        number_of_connected = width * height - 1
        index = -1
        
        while number_of_connected > 0:
            index += 1
            cell1 = SpanningTree.get_index(
                edges[index][0], edges[index][1], width)
            cell2 = SpanningTree.get_index(
                edges[index][2], edges[index][3], width)
            if (union_find.connected(cell1, cell2)):
                continue
            union_find.union(cell1, cell2)
            if (edges[index][4] == 0):
                maze.grid[edges[index][0]][edges[index][1]].right_wall = False
                maze.grid[edges[index][2]][edges[index][3]].left_wall = False
            elif (edges[index][4] == 1):
                maze.grid[edges[index][0]][edges[index][1]].left_wall = False
                maze.grid[edges[index][2]][edges[index][3]].right_wall = False
            elif (edges[index][4] == 2):
                maze.grid[edges[index][0]][edges[index][1]].bottom_wall = False
                maze.grid[edges[index][2]][edges[index][3]].top_wall = False
            elif (edges[index][4] == 3):
                maze.grid[edges[index][0]][edges[index][1]].top_wall = False
                maze.grid[edges[index][2]][edges[index][3]].bottom_wall = False
            number_of_connected -= 1

        return maze
