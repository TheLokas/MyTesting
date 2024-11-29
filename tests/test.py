import unittest
from io import StringIO
from unittest.mock import patch
from Maze import Maze
from MazeBFS import MazeSolver
from main import main
import os

class TestMaze(unittest.TestCase):

    def setUp(self):
        """Подготовка к тестам. Создание файлов с лабиринтами."""
        # Валидный лабиринт
        self.valid_maze = Maze()
        maze_data_valid = """0 1 0
                             0 1 0
                             0 0 0"""
        with open('valid_maze.txt', 'w') as f:
            f.write(maze_data_valid)

        # Невалидный лабиринт
        self.invalid_maze = Maze()
        maze_data_invalid = """0 1 0
                               0 2 0  # Неверный символ (2)
                               0 0 0"""
        with open('invalid_maze.txt', 'w') as f:
            f.write(maze_data_invalid)

    def tearDown(self):
        """Удаление файлов после тестов."""
        if os.path.exists('valid_maze.txt'):
            os.remove('valid_maze.txt')
        if os.path.exists('invalid_maze.txt'):
            os.remove('invalid_maze.txt')

    def test_load_from_file_valid(self):
        """Тест для загрузки валидного лабиринта."""
        self.valid_maze.load_from_file('valid_maze.txt')

        # Проверка, что лабиринт был загружен
        self.assertTrue(self.valid_maze.is_loaded)

        # Проверка, что лабиринт содержит правильные данные
        expected_maze = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertEqual(self.valid_maze.maze, expected_maze)

    def test_load_from_file_invalid(self):
        """Тест для загрузки невалидного лабиринта с ошибкой в формате."""
        self.invalid_maze.load_from_file('invalid_maze.txt')

        # Проверка, что лабиринт не был загружен из-за ошибки
        self.assertFalse(self.invalid_maze.is_loaded)

        # Проверка, что maze остался пустым (или None, в зависимости от вашей логики)
        self.assertEqual(self.invalid_maze.maze, [])


    def test_display_maze_valid(self):
        """Тест для отображения лабиринта при корректно загруженном лабиринте."""
        # Подготовка файла с валидным лабиринтом
        maze_data = """0 1 0
                       0 1 0
                       0 0 0"""
        with open('valid_maze.txt', 'w') as f:
            f.write(maze_data)

        # Создание экземпляра Maze и загрузка лабиринта
        self.maze = Maze()
        self.maze.load_from_file('valid_maze.txt')

        # Захват вывода в консоль
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.maze.display_maze()
            output = mock_stdout.getvalue()

        # Ожидаемый вывод
        expected_output = "Текущий лабиринт:\n0 1 0\n0 1 0\n0 0 0\n"

        # Проверка, что вывод совпадает с ожидаемым
        self.assertEqual(output, expected_output)

        # Удаление файла после теста
        if os.path.exists('valid_maze.txt'):
            os.remove('valid_maze.txt')

    def test_display_maze_not_loaded(self):
        """Тест для отображения сообщения об ошибке, если лабиринт не загружен."""
        # Захват вывода в консоль
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.maze = Maze()
            self.maze.display_maze()
            output = mock_stdout.getvalue()

        # Ожидаемый вывод
        expected_output = "Лабиринт не загружен. Загрузите лабиринт из файла.\n"

        # Проверка, что вывод совпадает с ожидаемым
        self.assertEqual(output, expected_output)

    def test_set_entry_and_exit_valid(self):
        """Тест для установки точек входа и выхода в корректном лабиринте."""
        # Подготовка файла с валидным лабиринтом
        maze_data = """0 1 0
                       0 1 0
                       0 0 0"""
        with open('valid_maze.txt', 'w') as f:
            f.write(maze_data)

        # Создание экземпляра Maze и загрузка лабиринта
        self.maze = Maze()
        self.maze.load_from_file('valid_maze.txt')

        # Патчинг ввода для теста (вводим точки входа и выхода)
        with patch('builtins.input', side_effect=['0,0', '2,2']), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.maze.set_entry_and_exit()
            output = mock_stdout.getvalue()

        # Ожидаемый вывод
        expected_output = "Точка входа установлена: (0, 0)\nТочка выхода установлена: (2, 2)\n"

        # Проверка, что вывод совпадает с ожидаемым
        self.assertEqual(output, expected_output)
        self.assertEqual(self.maze.entry_point, (0, 0))
        self.assertEqual(self.maze.exit_point, (2, 2))

        # Удаление файла после теста
        if os.path.exists('valid_maze.txt'):
            os.remove('valid_maze.txt')

    def test_set_entry_and_exit_invalid(self):
        """Тест для установки точек входа и выхода с неверными данными."""
        # Подготовка файла с валидным лабиринтом
        maze_data = """0 1 0
                       0 1 0
                       0 0 0"""
        with open('valid_maze.txt', 'w') as f:
            f.write(maze_data)

        # Создание экземпляра Maze и загрузка лабиринта
        self.maze = Maze()
        self.maze.load_from_file('valid_maze.txt')

        # Патчинг ввода для теста (вводим неверную точку входа и выхода)
        with patch('builtins.input', side_effect=['0,0', '2,3']), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.maze.set_entry_and_exit()
            output = mock_stdout.getvalue()

        # Ожидаемый вывод с ошибкой на точке выхода
        expected_output = "Неверная точка выхода. Попробуйте снова.\n"

        # Проверка, что вывод совпадает с ожидаемым
        self.assertEqual(output, expected_output)
        self.assertEqual(self.maze.entry_point, (0, 0))  # Точка входа должна быть установлена
        self.assertIsNone(self.maze.exit_point)  # Точка выхода не установлена

        # Удаление файла после теста
        if os.path.exists('valid_maze.txt'):
            os.remove('valid_maze.txt')

    def test_is_valid_point_valid(self):
        """Тест для проверки валидных точек внутри лабиринта."""

        # Создание лабиринта внутри теста
        maze = Maze()
        maze_data = """0 1 0
                       0 1 0
                       0 0 0"""
        maze.load_from_file('valid_maze.txt')

        # Проверка валидных точек, которые внутри лабиринта и проходимы (значение 0)
        valid_points = [
            (0, 0),  # верхний левый угол
            (2, 2),  # нижний правый угол
            (2, 1),  # точка на нижней линии, проходимая
        ]
        for point in valid_points:
            with self.subTest(point=point):
                self.assertTrue(maze._is_valid_point(point[0], point[1]))

    def test_is_valid_point_invalid(self):
        """Тест для проверки невалидных точек внутри лабиринта."""

        # Создание лабиринта внутри теста
        maze = Maze()
        maze_data = """0 1 0
                       0 1 0
                       0 0 0"""
        maze.load_from_file('valid_maze.txt')

        # Проверка невалидных точек
        invalid_points = [
            (-1, 0),  # выход за границы по X
            (0, -1),  # выход за границы по Y
            (3, 0),  # выход за границы по X
            (0, 3),  # выход за границы по Y
            (0, 1),  # точка на стене (непроходимая)
            (1, 1),  # точка на стене (непроходимая)
        ]
        for point in invalid_points:
            with self.subTest(point=point):
                self.assertFalse(maze._is_valid_point(point[0], point[1]))


class TestMazeSolver(unittest.TestCase):

    def test_is_valid_with_valid_points(self):
        """Тест для метода is_valid с валидными точками."""

        # Подготовка лабиринта внутри теста
        maze_data = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        entry = (0, 0)
        exit_ = (2, 2)
        solver = MazeSolver(maze_data, entry, exit_)

        # Валидные точки (должны возвращать True)
        valid_points = [
            (0, 0),  # Точка входа, проходимая
            (2, 2),  # Точка выхода, проходимая
            (2, 1),  # Проходимая точка внизу
            (1, 0),  # Проходимая точка сбоку
        ]
        for point in valid_points:
            with self.subTest(point=point):
                self.assertTrue(solver.is_valid(point[0], point[1]))

    def test_is_valid_with_invalid_points(self):
        """Тест для метода is_valid с невалидными точками."""

        # Подготовка лабиринта внутри теста
        maze_data = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        entry = (0, 0)
        exit_ = (2, 2)
        solver = MazeSolver(maze_data, entry, exit_)

        # Невалидные точки (должны возвращать False)
        invalid_points = [
            (-1, 0),  # Выход за пределы лабиринта (по X)
            (0, -1),  # Выход за пределы лабиринта (по Y)
            (3, 0),  # Выход за пределы лабиринта (по X)
            (0, 3),  # Выход за пределы лабиринта (по Y)
            (0, 1),  # Стена (непроходимая точка)
            (1, 1),  # Стена (непроходимая точка)
        ]
        for point in invalid_points:
            with self.subTest(point=point):
                self.assertFalse(solver.is_valid(point[0], point[1]))


    def test_find_shortest_path_valid(self):
        """Тест для метода find_shortest_path с валидным лабиринтом."""

        # Подготовка лабиринта внутри теста
        maze_data = [
            [0, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 0],
            [1, 1, 0, 0]
        ]
        entry = (0, 0)
        exit_ = (2, 3)
        solver = MazeSolver(maze_data, entry, exit_)

        # Ожидаемый кратчайший путь
        expected_path = [
            (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)
        ]

        # Проверка кратчайшего пути
        self.assertEqual(solver.find_shortest_path(), expected_path)

    def test_find_shortest_path_no_path(self):
        """Тест для метода find_shortest_path, когда пути нет."""

        # Подготовка лабиринта внутри теста
        maze_data = [
            [0, 1, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0],
            [1, 1, 0, 1]
        ]
        entry = (0, 0)
        exit_ = (3, 3)  # Выход заблокирован стенами
        solver = MazeSolver(maze_data, entry, exit_)

        # Проверка, что путь не найден
        self.assertIsNone(solver.find_shortest_path())

    def test_find_shortest_path_start_is_exit(self):
        """Тест для метода find_shortest_path, когда точка входа совпадает с точкой выхода."""

        # Подготовка лабиринта внутри теста
        maze_data = [
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        entry = (0, 0)
        exit_ = (0, 0)  # Точка входа совпадает с выходом
        solver = MazeSolver(maze_data, entry, exit_)

        # Ожидаемый кратчайший путь: точка входа сразу является выходом
        expected_path = [(0, 0)]

        # Проверка кратчайшего пути
        self.assertEqual(solver.find_shortest_path(), expected_path)

    def test_reconstruct_path_valid(self):
        """Тест для метода reconstruct_path с валидным путем."""

        # Подготовка лабиринта внутри теста
        maze_data = [
            [0, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 0],
            [1, 1, 0, 0]
        ]
        entry = (0, 0)
        exit_ = (2, 3)
        solver = MazeSolver(maze_data, entry, exit_)

        # Пример пути
        path = [
            (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)
        ]

        # Ожидаемое преобразованное представление пути
        expected_output = "Путь: (0, 0) -> (1, 0) -> (2, 0) -> (2, 1) -> (2, 2) -> (2, 3)\nДлина пути: 5 шагов"

        # Проверка корректности преобразования пути
        self.assertEqual(solver.reconstruct_path(path), expected_output)

    def test_reconstruct_path_no_path(self):
        """Тест для метода reconstruct_path, когда пути нет."""

        # Подготовка лабиринта внутри теста
        maze_data = [
            [0, 1, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0],
            [1, 1, 0, 1]
        ]
        entry = (0, 0)
        exit_ = (3, 3)  # Выход заблокирован стенами
        solver = MazeSolver(maze_data, entry, exit_)

        # Путь не найден, поэтому передаем пустой список
        path = []

        # Ожидаемый результат
        expected_output = "Путь не найден."

        # Проверка, что вывод правильный
        self.assertEqual(solver.reconstruct_path(path), expected_output)

    def test_reconstruct_path_single_step(self):
        """Тест для метода reconstruct_path, когда путь состоит из одного шага (вход совпадает с выходом)."""

        # Подготовка лабиринта внутри теста
        maze_data = [
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        entry = (0, 0)
        exit_ = (0, 0)  # Точка входа совпадает с точкой выхода
        solver = MazeSolver(maze_data, entry, exit_)

        # Путь состоит из одного шага
        path = [(0, 0)]

        # Ожидаемый результат
        expected_output = "Путь: (0, 0)\nДлина пути: 0 шагов"

        # Проверка, что вывод правильный
        self.assertEqual(solver.reconstruct_path(path), expected_output)



if __name__ == '__main__':
    unittest.main()
