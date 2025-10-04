def greedy_algorithm(items, budget):
    # Сортуємо за співвідношенням калорій/вартість у спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    total_cost = 0
    total_calories = 0
    selected_items = []

    for name, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(name)
            total_cost += info["cost"]
            total_calories += info["calories"]

    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories
    }

def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    # dp[i][j] — максимальна калорійність при використанні перших i предметів і бюджеті j
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, info = item_list[i - 1]
        cost = info["cost"]
        calories = info["calories"]
        for j in range(budget + 1):
            if cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
            else:
                dp[i][j] = dp[i - 1][j]

    # Відновлення вибраних предметів
    selected_items = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            name, info = item_list[i - 1]
            selected_items.append(name)
            j -= info["cost"]

    total_calories = dp[n][budget]
    total_cost = sum(items[item]["cost"] for item in selected_items)

    return {
        "selected_items": selected_items[::-1],  # у правильному порядку
        "total_cost": total_cost,
        "total_calories": total_calories
    }

def demo_meal_budget():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100

    print("=== DEMO: Вибір їжі при бюджеті", budget, "===\n")

    print("Жадібний алгоритм:")
    greedy_result = greedy_algorithm(items, budget)
    print("Вибрані страви:", greedy_result["selected_items"])
    print("Загальна вартість:", greedy_result["total_cost"])
    print("Загальна калорійність:", greedy_result["total_calories"])
    print()

    print("Динамічне програмування:")
    dp_result = dynamic_programming(items, budget)
    print("Вибрані страви:", dp_result["selected_items"])
    print("Загальна вартість:", dp_result["total_cost"])
    print("Загальна калорійність:", dp_result["total_calories"])

if __name__ == "__main__":
    demo_meal_budget()