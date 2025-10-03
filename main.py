from task1_linked_list import demo_linked_list
# from task2_fractal_tree import draw_fractal_tree
# інші імпорти за потреби

def main():
    print("Фінальний проєкт. Виберіть завдання:")
    print("1 - Однозв'язний список")
    print("2 - Фрактальне дерево")
    # ...
    choice = input("Ваш вибір: ")

    if choice == "1":
        demo_linked_list()
    # elif choice == "2":
    #     draw_fractal_tree()
    # ...

if __name__ == "__main__":
    main()