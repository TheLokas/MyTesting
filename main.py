from MazeGenerator import MazeGenerator
from MazeBFS import MazeSolver, get_user_input


if __name__ == "__main__":
    print("Добро пожаловать в генератор лабиринтов!")
    rows = get_user_input("Введите количество строк лабиринта: ")
    cols = get_user_input("Введите количество столбцов лабиринта: ")

    generator = MazeGenerator(rows, cols)
    generator.generate_maze()
    entry, exit = generator.set_entry_and_exit()
    print(f"Вход: {entry}, Выход: {exit}")
    generator.print_maze()

    solver = MazeSolver(generator.maze, entry, exit)
    path = solver.find_shortest_path()
    if path:
        print("\nНайденный путь:")
        solver.print_path(path)
    else:
        print("\nПуть не найден!")



# Исправить ошибку, что вход и выход может сгенерироваться в углах (мб и не надо)
# Дописать позитивные и негативные тесты для поиск в ширину
# написать интеграционные тесты
