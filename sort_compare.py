import argparse
# other imports go here

import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order."""
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def insertion_sort(a_list):
    """Perform insertion sort on a list."""
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

def shell_sort(a_list):
    """Perform shell sort on a list."""
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    """Helper function for shell sort that performs insertion sort on gap-separated elements."""
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value

def python_sort(a_list):
    """Wrapper for Python's built-in sort."""
    return sorted(a_list)

def benchmark_sort(the_size):
    """Benchmark sorting algorithms on random lists of size the_size."""
    
    # Python Sort
    total_time = 0
    for _ in range(100):
        mylist = get_me_random_list(the_size)
        start = time.time()
        python_sort(mylist)
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"Python sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

    # Insertion Sort
    total_time = 0
    for _ in range(100):
        mylist = get_me_random_list(the_size)
        start = time.time()
        insertion_sort(mylist)
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"Insertion sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

    # Shell Sort
    total_time = 0
    for _ in range(100):
        mylist = get_me_random_list(the_size)
        start = time.time()
        shell_sort(mylist)
        time_spent = time.time() - start
        total_time += time_spent
    avg_time = total_time / 100
    print(f"Shell sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

if __name__ == "__main__":
    """Main entry point."""
    list_sizes = [500, 1000, 5000]

    for the_size in list_sizes:
        print(f"\nBenchmarking for list size: {the_size}")
        benchmark_sort(the_size)