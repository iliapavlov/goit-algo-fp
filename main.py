from task1_linked_list import demo_linked_list
from task2_fractal_tree import draw_fractal_tree
from task3_dejkstra import demo_dejkstra
from task4_visualize_heap import demo_heap_visualization
from task5_visualize_search import demo_traversal_visualization
from task6_maximize_calories import demo_meal_budget
from task7_monte_carlo_dice import demo_monte_carlo

def main():
    print("Фінальний проєкт. Виберіть завдання:")
    print("1 - Однозв'язний список")
    print("2 - Фрактальне дерево")
    print("3 - Алгоритм Дейкстри")
    print("4 - Візуалізація бінарної купи")
    print("5 - Візуалізація пошуку в бінарному дереві (DFS та BFS)")
    print("6 - Максимізація калорій при обмеженому бюджеті")
    print("7 - Метод Монте-Карло для двох кубиків")
    print("0 - Вийти")

    choice = input("Ваш вибір: ")

    match choice:
        case "1":
            demo_linked_list()
        case "2":
            draw_fractal_tree()
        case "3":
            demo_dejkstra()
        case "4":
            demo_heap_visualization()
        case "5":
            demo_traversal_visualization()
        case "6":
            demo_meal_budget()
        case "7":
            demo_monte_carlo()
        case "0":
            print("Вихід з програми.")
        case _:
            print("Некоректний вибір. Завершення програми.")

if __name__ == "__main__":
    main()