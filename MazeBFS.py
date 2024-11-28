from collections import deque

class MazeSolver:
    def __init__(self, maze, entry, exit):
        self.maze = maze
        self.entry = entry
        self.exit = exit
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Возможные направления: вправо, вниз, влево, вверх

    def find_shortest_path(self):
        """Находит кратчайший путь от точки входа до выхода."""
        queue = deque([(self.entry, [self.entry])])
        visited = set()
        visited.add(self.entry)

        while queue:
            (current_row, current_col), path = queue.popleft()

            if (current_row, current_col) == self.exit:
                return path  # Возвращаем путь, когда достигнут выход

            for dr, dc in self.directions:
                new_row, new_col = current_row + dr, current_col + dc

                if 0 <= new_row < self.rows and 0 <= new_col < self.cols and \
                   self.maze[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append(((new_row, new_col), path + [(new_row, new_col)]))

        return []  # Возвращаем пустой список, если пути нет

    def print_path(self, path):
        """Выводит длину пути."""
        if len(path)>0:
            print(f"Длина пути: {len(path)}")
        else:
            print('Нет пути от входа до выхода.')

def get_user_input(prompt):
    """Запрашивает ввод у пользователя и проверяет, что он корректен."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 2:
                raise ValueError("Размер должен быть положительным числом")
            return value
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")
