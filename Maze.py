class Maze:
    def __init__(self):
        self.maze = []  # Лабиринт в виде двумерного массива
        self.entry_point = None  # Точка входа
        self.exit_point = None  # Точка выхода
        self.is_loaded = False  # Флаг успешной загрузки лабиринта

    def load_from_file(self, filename):
        """
        Метод считывает лабиринт из текстового файла.
        Проверяет, чтобы каждая строка содержала только числа 1 и 0, разделенные пробелами.
        """
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                maze = []

                for line in lines:
                    line = line.strip()
                    if not line:
                        continue  # Игнорируем пустые строки
                    # Проверяем, чтобы строка содержала только 1 и 0, разделенные пробелами
                    if not all(cell in {"1", "0"} for cell in line.split()):
                        raise ValueError(f"Неверный формат строки: '{line}'. Ожидаются только числа 1 и 0.")

                    # Преобразуем строку в список чисел
                    maze.append(list(map(int, line.split())))

                # Проверяем, чтобы все строки имели одинаковую длину
                row_length = len(maze[0])
                if not all(len(row) == row_length for row in maze):
                    raise ValueError("Лабиринт должен быть прямоугольным (все строки одинаковой длины).")

                self.maze = maze
                self.is_loaded = True  # Устанавливаем флаг успешной загрузки
                print("Лабиринт успешно загружен!")

        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
        except ValueError as e:
            print(f"Ошибка: {e}")
            self.is_loaded = False  # Сбрасываем флаг успешной загрузки

    def display_maze(self):
        """
        Метод для отображения лабиринта в консоли.
        """

        print("Текущий лабиринт:")
        for row in self.maze:
            print(' '.join(map(str, row)))

    def set_entry_and_exit(self):
        """
        Метод для установки точек входа и выхода для лабиринта.
        """
        if not self.is_loaded:
            print("Лабиринт не загружен. Загрузите лабиринт из файла.")
            return

        try:
            # Ввод точки входа
            entry = input("Введите точку входа (x, y): ").strip()
            entry_x, entry_y = map(int, entry.split(','))
            if self._is_valid_point(entry_x, entry_y):
                self.entry_point = (entry_x, entry_y)
            else:
                print("Неверная точка входа. Попробуйте снова.")
                return

            # Ввод точки выхода
            exit_ = input("Введите точку выхода (x, y): ").strip()
            exit_x, exit_y = map(int, exit_.split(','))
            if self._is_valid_point(exit_x, exit_y):
                self.exit_point = (exit_x, exit_y)
            else:
                print("Неверная точка выхода. Попробуйте снова.")
                return

            print(f"Точка входа установлена: {self.entry_point}")
            print(f"Точка выхода установлена: {self.exit_point}")

        except ValueError:
            print("Ошибка ввода. Укажите координаты в формате x, y.")

    def _is_valid_point(self, x, y):
        """
        Проверяет, находится ли точка (x, y) внутри лабиринта и является ли она проходимой (0).
        """
        return 0 <= x < len(self.maze) and 0 <= y < len(self.maze[0]) and self.maze[x][y] == 0
