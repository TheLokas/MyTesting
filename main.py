from Maze import Maze
from MazeBFS import MazeSolver


def main():
    maze = Maze()

    # Чтение лабиринта из файла
    maze.load_from_file("maze.txt")

    # Вывод лабиринта
    maze.display_maze()

    # Установка точек входа и выхода
    maze.set_entry_and_exit()

    # Если лабиринт успешно загружен и точки входа/выхода заданы
    if maze.is_loaded and maze.entry_point and maze.exit_point:
        # Инициализация решателя лабиринта
        solver = MazeSolver(maze.maze, maze.entry_point, maze.exit_point)

        # Поиск кратчайшего пути
        path = solver.find_shortest_path()

        # Вывод пути или сообщение об отсутствии пути
        print(solver.reconstruct_path(path))


if __name__ == "__main__":
    main()