import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    # Симуляція кидків
    counts = {i: 0 for i in range(2, 13)}  # можливі суми від 2 до 12

    for _ in range(num_rolls):
        # Кидок двох кубіків, рівномірний розподіл цілого числа від 1 до 6
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        # Підрахунок кількості кидків для можливих значень сум
        counts[roll_sum] += 1

    # Обрахування ймовірності випаду кожної суми
    probabilities = {s: counts[s] / num_rolls for s in counts}

    return probabilities


def plot_probabilities(probabilities):
    import matplotlib.pyplot as plt

    # Аналітичні ймовірності
    analytical = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
        7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }

    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    ana_probs = [analytical[s] for s in sums]

    # Створення графіка
    plt.figure(figsize=(10, 6))
    plt.bar(sums, probs, tick_label=sums, color='skyblue', label='Монте-Карло')
    plt.plot(sums, ana_probs, color='red', marker='o', linestyle='-', label='Аналітичні')

    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках')

    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob + 0.002, f"{prob*100:.2f}%", ha='center', fontsize=9)

    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

def demo_monte_carlo():
    print("=== Демонстрація методу Монте-Карло для двох кубиків ===")
    for accuracy in [100, 1000, 10000, 100000]:
        print(f"\nСимуляція для {accuracy} кидків:")
        probabilities = simulate_dice_rolls(accuracy)
        plot_probabilities(probabilities)

if __name__ == "__main__":
    demo_monte_carlo()