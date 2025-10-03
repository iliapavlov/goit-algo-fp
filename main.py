from task1_linked_list import demo_linked_list
from task2_fractal_tree import draw_fractal_tree
from task3_dejkstra import demo_dejkstra
# ...

def main():
    print("Фінальний проєкт. Виберіть завдання:")
    print("1 - Однозв'язний список")
    print("2 - Фрактальне дерево")
    print("3 - Алгоритм Дейкстри")
    # ...
    choice = input("Ваш вибір: ")

    match choice:
        case "1":
            demo_linked_list()
        case "2":
            draw_fractal_tree()
        case "3":
            demo_dejkstra()
        case _:
            print("Некоректний вибір. Завершення програми.")

if __name__ == "__main__":
    main()