from collections import deque

class MazeSolver:
    def __init__(self, maze, entry, exit_):
        """
        Инициализация решателя лабиринта.
        :param maze: Двумерный массив, представляющий лабиринт (0 - проходимый, 1 - стена).
        :param entry: Точка входа (x, y).
        :param exit_: Точка выхода (x, y).
        """
        self.maze = maze
        self.entry = entry
        self.exit = exit_
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Список возможных направлений: вверх, вниз, влево, вправо

    def is_valid(self, x, y):
        """
        Проверяет, можно ли перейти в указанную точку.
        :param x: Координата X.
        :param y: Координата Y.
        :return: True, если точка в пределах лабиринта и проходима, иначе False.
        """
        rows, cols = len(self.maze), len(self.maze[0])
        return 0 <= x < rows and 0 <= y < cols and self.maze[x][y] == 0

    def find_shortest_path(self):
        """
        Реализация поиска в ширину (BFS) для нахождения кратчайшего пути.
        :return: Список координат кратчайшего пути от точки входа до точки выхода или None, если пути нет.
        """
        queue = deque([(self.entry, [])])  # Очередь: ((x, y), путь до текущей точки)
        visited = set()  # Множество посещённых точек
        visited.add(self.entry)

        while queue:
            (current, path) = queue.popleft()
            path = path + [current]

            # Если мы достигли выхода, возвращаем путь
            if current == self.exit:
                return path

            # Проверяем все возможные направления
            for dx, dy in self.directions:
                nx, ny = current[0] + dx, current[1] + dy
                if self.is_valid(nx, ny) and (nx, ny) not in visited:
                    queue.append(((nx, ny), path))
                    visited.add((nx, ny))

        # Если выхода нет, возвращаем None
        return None

    def reconstruct_path(self, path):
        """
        Преобразует путь в удобный для чтения вид и возвращает его длину.
        :param path: Список координат пути.
        :return: Строка, представляющая путь и его длину.
        """
        if not path:
            return "Путь не найден."

        # Преобразуем путь в строку
        path_str = " -> ".join([f"({x}, {y})" for x, y in path])
        path_length = len(path) - 1  # Длина пути: количество шагов (минус 1, если путь состоит из точек)

        return f"Путь: {path_str}\nДлина пути: {path_length} шагов"

