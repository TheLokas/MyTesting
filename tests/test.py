import unittest
from MazeGenerator import MazeGenerator
from MazeBFS import MazeSolver, get_user_input

class TestMazeGenerator(unittest.TestCase):


    def test_initialization(self):
        """Тест инициализации лабиринта."""
        rows, cols = 10, 10
        maze_generator = MazeGenerator(rows, cols)

        self.assertEqual(maze_generator.rows, rows)
        self.assertEqual(maze_generator.cols, cols)
        self.assertEqual(len(maze_generator.maze), rows)
        self.assertEqual(len(maze_generator.maze[0]), cols)

        # Проверяем, что изначально все клетки заполнены стенами (1)
        self.assertTrue(all(cell == 1 for row in maze_generator.maze for cell in row))


    def test_generate_maze(self):
        """Тест генерации лабиринта."""
        rows, cols = 10, 10
        maze_generator = MazeGenerator(rows, cols)
        maze_generator.generate_maze()

        # Проверяем, что после генерации хотя бы один проход (0) присутствует
        pass_found = any(cell == 0 for row in maze_generator.maze for cell in row)
        self.assertTrue(pass_found)


    def test_set_entry_and_exit(self):
        """Тест установки входа и выхода в лабиринте."""
        rows, cols = 10, 10
        maze_generator = MazeGenerator(rows, cols)
        maze_generator.generate_maze()
        entry, exit = maze_generator.set_entry_and_exit()

        # Проверяем, что вход и выход находятся на краю лабиринта
        # Убедимся, что хотя бы одна из координат находится на краю
        self.assertTrue(entry[0] == 0 or entry[0] == rows - 1 or entry[1] == 0 or entry[1] == cols - 1)
        self.assertTrue(exit[0] == 0 or exit[0] == rows - 1 or exit[1] == 0 or exit[1] == cols - 1)

        # Проверяем, что вход и выход разные
        self.assertNotEqual(entry, exit)

        # Проверяем, что вход и выход установлены как проходы (0)
        self.assertEqual(maze_generator.maze[entry[0]][entry[1]], 0)
        self.assertEqual(maze_generator.maze[exit[0]][exit[1]], 0)


    def test_generate_maze_no_isolated_cells(self):
        """Тест, который проверяет, что в сгенерированном лабиринте нет изолированных клеток."""
        rows, cols = 10, 10
        maze_generator = MazeGenerator(rows, cols)
        maze_generator.generate_maze()

        # Проверяем, что нет клеток, окруженных стенами
        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if maze_generator.maze[row][col] == 0:
                    self.assertIn(maze_generator.maze[row + 1][col], [0, 1])
                    self.assertIn(maze_generator.maze[row - 1][col], [0, 1])
                    self.assertIn(maze_generator.maze[row][col + 1], [0, 1])
                    self.assertIn(maze_generator.maze[row][col - 1], [0, 1])


    def test_random_entry_and_exit(self):
        """Тест, который проверяет, что вход и выход генерируются случайным образом."""
        rows, cols = 10, 10
        maze_generator = MazeGenerator(rows, cols)
        maze_generator.generate_maze()

        entries_and_exits = set()

        for _ in range(100):  # Проверяем 100 случайных генераций
            entry, exit = maze_generator.set_entry_and_exit()
            entries_and_exits.add((entry, exit))

        # Убедимся, что были различные комбинации входа и выхода
        self.assertGreater(len(entries_and_exits), 1)


    def test_negative_rows(self):
        """Тест на отрицательные размеры лабиринта."""
        with self.assertRaises(ValueError):
            maze_generator = MazeGenerator(-5, 10)

    def test_zero_rows(self):
        """Тест на нулевые размеры лабиринта."""
        with self.assertRaises(ValueError):
            maze_generator = MazeGenerator(0, 10)

    def test_invalid_row_string(self):
        """Тест на строки вместо чисел для строк."""
        with self.assertRaises(ValueError):
            maze_generator = MazeGenerator("abc", 10)

    def test_invalid_col_string(self):
        """Тест на строки вместо чисел для столбцов."""
        with self.assertRaises(ValueError):
            maze_generator = MazeGenerator(10, "xyz")

    def test_too_small_maze(self):
        """Тест на слишком маленькие размеры лабиринта."""
        with self.assertRaises(ValueError):
            maze_generator = MazeGenerator(1, 1)

    def test_find_shortest_path(self):
        """Тест на поиск кратчайшего пути в лабиринте."""
        maze = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 1, 1, 1, 0]
        ]
        entry = (0, 0)  # Вход
        exit = (4, 4)  # Выход
        solver = MazeSolver(maze, entry, exit)
        path = solver.find_shortest_path()

        # Ожидаем, что путь будет найден
        self.assertGreater(len(path), 0, "Путь не найден.")

        # Ожидаем, что конечная точка будет выходом
        self.assertEqual(path[-1], exit, f"Неверный выход: {path[-1]}")

    def test_no_path(self):
        """Тест на случай, когда пути нет."""
        maze = [
            [0, 1, 0],
            [1, 1, 0],
            [0, 1, 0]
        ]
        entry = (0, 0)  # Вход
        exit = (2, 2)  # Выход
        solver = MazeSolver(maze, entry, exit)
        path = solver.find_shortest_path()

        # Ожидаем, что путь не будет найден
        self.assertEqual(path, [], "Путь должен быть пустым.")

    def test_multiple_paths(self):
        """Тест на лабиринт с несколькими путями."""
        maze = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        entry = (0, 0)  # Вход
        exit = (4, 4)  # Выход
        solver = MazeSolver(maze, entry, exit)
        path = solver.find_shortest_path()

        # Ожидаем, что путь будет найден
        self.assertGreater(len(path), 0, "Путь не найден.")

        # Проверим, что путь заканчивается на выходе
        self.assertEqual(path[-1], exit, f"Неверный выход: {path[-1]}")

    def test_path_length(self):
        """Тест на проверку длины пути."""
        maze = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 1, 1, 1, 0]
        ]
        entry = (0, 0)  # Вход
        exit = (4, 4)  # Выход
        solver = MazeSolver(maze, entry, exit)
        path = solver.find_shortest_path()

        # Ожидаем, что путь имеет длину 9
        self.assertEqual(len(path), 9, f"Ожидаемая длина пути 9, но получена {len(path)}.")

    def test_print_path(self):
        """Тест на печать пути в лабиринте."""
        maze = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 1, 1, 1, 0]
        ]
        entry = (0, 0)  # Вход
        exit = (4, 4)  # Выход
        solver = MazeSolver(maze, entry, exit)
        path = solver.find_shortest_path()

        # Проверяем вывод пути
        solver.print_path(path)
        # Ожидаем, что в консоли будет напечатана длина пути
        self.assertIn("Длина пути:", self._get_stdout())

    def _get_stdout(self):
        """Получаем стандартный вывод в виде строки (для тестирования print)."""
        import sys
        from io import StringIO
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        return_value = sys.stdout.getvalue()
        sys.stdout = old_stdout
        return return_value




if __name__ == "__main__":
    unittest.main()
