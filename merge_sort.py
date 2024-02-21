import random
import timeit

def merge_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    mid = n // 2
    left_lst = lst[:mid]
    right_lst = lst[mid:]
    
    return merge(merge_sort(left_lst), merge_sort(right_lst))


def merge(left_lst, right_lst):
    
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left_lst) and right_idx < len(right_lst):
        if left_lst[left_idx] <= right_lst[right_idx]:
            merged.append(left_lst[left_idx])
            left_idx += 1
        else:
            merged.append(right_lst[right_idx])
            right_idx += 1

    merged.extend(left_lst[left_idx:])
    merged.extend(right_lst[right_idx:])
    
    return merged
small_arr = [5, 3, 8, 4, 2]
average_arr = [7, 12, 3, 5, 8, 11, 20, 1, 6, 14]
big_arr = [random.randint(1, 1000) for _ in range(10000)]

small_sorted_arr = merge_sort(small_arr)
average_sorted_arr = merge_sort(average_arr)
big_sorted_arr = merge_sort(big_arr)


print(small_sorted_arr)
print(average_sorted_arr)
# print(big_sorted_arr)

time_taken_small = timeit.timeit(lambda: merge_sort(small_arr), number=1000)
time_taken_average = timeit.timeit(lambda: merge_sort(average_arr), number=1000)
time_taken_big = timeit.timeit(lambda: merge_sort(big_arr), number=1000)

print(f"Time taken: {time_taken_small} seconds")
print(f"Time taken: {time_taken_average} seconds")
print(f"Time taken: {time_taken_big} seconds")
