import heapq
from Maze import Maze
from Path import Path


class AStar:
    def solve(maze: Maze) -> Path:
        edges = maze.get_edges()
        stack = []
        heapq.heappush(stack, (0, 0, 0))
        path = Path(maze)
        distance: list[list[int]] = [[]]
        prev: list[list[tuple[int, int]]] = [[]]
        for i in range(maze.height):
            distance.append([])
            prev.append([])
            for j in range(maze.width):
                distance[i].append(maze.height * maze.width + 2)
                prev[i].append((-1, -1))

        top_cell = (maze.height - 1, maze.width - 1)
        while len(stack) > 0:
            (current_dist, top_x, top_y) = heapq.heappop(stack)
            current_dist -= int(((maze.height - 1 - top_x)
                                ** 2 + (maze.width - 1 - top_x)**2)**0.5)
            for (cell_x, cell_y, wall_type) in edges[top_x][top_y]:
                if distance[cell_x][cell_y] <= current_dist + 1:
                    continue
                distance[cell_x][cell_y] = current_dist + 1
                heapq.heappush(stack, (current_dist + 1 + int(((maze.height - 1 - cell_x)
                               ** 2 + (maze.width - 1 - cell_x)**2)**0.5), cell_x, cell_y))
                prev[cell_x][cell_y] = (top_x, top_y)
                if (cell_x, cell_y) == top_cell:
                    stack.clear()

        cell = top_cell
        path.append(top_cell[0], top_cell[1])
        while cell != (0, 0):
            cell = prev[cell[0]][cell[1]]
            path.append(cell[0], cell[1])

        path.path.reverse()
        return path
