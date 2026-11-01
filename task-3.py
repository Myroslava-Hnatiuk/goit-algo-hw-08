
import heapq

def min_cable_cost(cables):
    # Перетворюємо список на Min Heap
    heapq.heapify(cables)

    total_cost = 0

    # Поки не залишиться один кабель
    while len(cables) > 1:

        # Дістаємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Об'єднуємо їх
        merged = first + second

        # Додаємо вартість об'єднання
        total_cost += merged

        # Повертаємо новий кабель у купу
        heapq.heappush(cables, merged)

    return total_cost


cables = [1, 2, 5, 11, 14]

print(min_cable_cost(cables))
