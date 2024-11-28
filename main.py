from MazeGenerator import MazeGenerator
from MazeBFS import MazeSolver, get_user_input


def main():
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


if __name__ == "__main__":
    main()