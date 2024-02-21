import timeit
import random

small_arr = [5, 3, 8, 4, 2]
average_arr = [7, 12, 3, 5, 8, 11, 20, 1, 6, 14]
big_arr = [random.randint(1, 1000) for _ in range(10000)]

small_arr.sort()
average_arr.sort()
big_arr.sort()

print(small_arr)
print(average_arr)
# print(big_arr)


time_taken_small = timeit.timeit(lambda: small_arr.sort(), number=1000)
time_taken_average = timeit.timeit(lambda: average_arr.sort(), number=1000)
time_taken_big = timeit.timeit(lambda: big_arr.sort(), number=1000)

print(f"Time taken: {time_taken_small} seconds")
print(f"Time taken: {time_taken_average} seconds")
print(f"Time taken: {time_taken_big} seconds\n")

time_taken_small = timeit.timeit(lambda: sorted(small_arr), number=1000)
time_taken_average = timeit.timeit(lambda: sorted(average_arr), number=1000)
time_taken_big = timeit.timeit(lambda: sorted(big_arr), number=1000)

print(f"Time taken: {time_taken_small} seconds")
print(f"Time taken: {time_taken_average} seconds")
print(f"Time taken: {time_taken_big} seconds")
