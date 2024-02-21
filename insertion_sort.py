import random
import timeit

def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]             
        j = i -1
        while j >= 0 and key < l[j]:  
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
        
    return l


small_arr = [5, 3, 8, 4, 2]
average_arr = [7, 12, 3, 5, 8, 11, 20, 1, 6, 14]
big_arr = [random.randint(1, 1000) for _ in range(10000)]

small_sorted_arr = insertion_sort(small_arr)
average_sorted_arr = insertion_sort(average_arr)
big_sorted_arr = insertion_sort(big_arr)

print(small_sorted_arr)
print(average_sorted_arr)
# print(big_sorted_arr)

time_taken_small = timeit.timeit(lambda: insertion_sort(small_arr), number=1000)
time_taken_average = timeit.timeit(lambda: insertion_sort(average_arr), number=1000)
time_taken_big = timeit.timeit(lambda: insertion_sort(big_arr), number=1000)

print(f"Time taken: {time_taken_small} seconds")
print(f"Time taken: {time_taken_average} seconds")
print(f"Time taken: {time_taken_big} seconds")