# Дано k відсортованих списків цілих чисел. Ваше завдання — об'єднати їх у один відсортований список. Реалізуйте функцію
# 'merge_k_lists , яка приймає на вхід список відсортованих списків та повертає відсортований список.)

import heapq


def merge_k_lists(lists):
    merged_list = []
    heap = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        merged_list.append(val)
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(heap, next_tuple)

    return merged_list


# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)




