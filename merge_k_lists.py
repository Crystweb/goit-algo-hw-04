# Дано k відсортованих списків цілих чисел. Ваше завдання — об'єднати їх у один відсортований список. Реалізуйте функцію
# 'merge_k_lists , яка приймає на вхід список відсортованих списків та повертає відсортований список.)

import heapq


def merge_k_lists(lists):
    merged_list = []
    heap = []

    # Додавання перших елементів з кожного списку в heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    # Обробка heap до повного злиття всіх списків
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        merged_list.append(val)
        # Додавання наступного елемента зі списку, звідки був взятий поточний елемент
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(heap, next_tuple)

    return merged_list


# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [20, 6], [50, 13, 84], [200, 600, 87]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)

