import random


class MazeGenerator:
    def __init__(self, rows, cols):
        # Проверка на корректность входных данных
        if not isinstance(rows, int) or not isinstance(cols, int):
            raise ValueError("Размеры должны быть целыми числами.")
        if rows <= 2 or cols <= 2:
            raise ValueError("Размеры лабиринта должны быть больше 2.")
        self.rows = rows
        self.cols = cols
        self.maze = [[1 for _ in range(cols)] for _ in range(rows)]  # Изначально вся матрица состоит из стен (1)


    def generate_maze(self):
        """Генерирует лабиринт с использованием алгоритма обратной трассировки пути."""
        start_row, start_col = random.randint(1, self.rows - 2), random.randint(1, self.cols - 2)
        self._carve_passage(start_row, start_col)


    def _carve_passage(self, row, col):
        """Рекурсивный метод для создания проходов в лабиринте."""
        self.maze[row][col] = 0  # Устанавливаем текущую ячейку как проход (0)
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]  # Возможные направления: вверх, вниз, влево, вправо
        random.shuffle(directions)  # Перемешиваем направления, чтобы сделать лабиринт случайным

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 1 <= new_row < self.rows - 1 and 1 <= new_col < self.cols - 1 and self.maze[new_row][new_col] == 1:
                # Проверяем, что мы не вышли за пределы и не посещали эту ячейку
                wall_row, wall_col = row + dr // 2, col + dc // 2  # Координаты стены между ячейками
                self.maze[wall_row][wall_col] = 0  # Убираем стену
                self._carve_passage(new_row, new_col)


    def set_entry_and_exit(self):
        """Устанавливает случайный вход и выход на краях лабиринта."""
        edges = [(0, i) for i in range(1, self.cols - 1)] + \
                [(self.rows - 1, i) for i in range(1, self.cols - 1)] + \
                [(i, 0) for i in range(1, self.rows - 1)] + \
                [(i, self.cols - 1) for i in range(1, self.rows - 1)]

        entry = random.choice(edges)
        exit = random.choice(edges)
        while exit == entry:  # Убедимся, что вход и выход разные
            exit = random.choice(edges)

        self.maze[entry[0]][entry[1]] = 0
        self.maze[exit[0]][exit[1]] = 0
        return entry, exit


    def print_maze(self):
        """Выводит лабиринт на экран."""
        for row in self.maze:
            print(row)


