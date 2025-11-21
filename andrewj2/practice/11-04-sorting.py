import sys
import time
import random

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

# SELECTION SORT
def selection(arr):
    # start from 1st element
    for i in range(len(arr)-1):
        min_idx = i
        # loop from start index to end of list and update min index
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # swap start index and min index
        swap(arr, i, min_idx)

# INSERTION SORT
def insertion(arr):
    # start after 1st element
    for i in range(1, len(arr)):
        j = i
        # loop backwards, swapping values
        while j > 0 and arr[j-1] > arr[j]:
            swap(arr, j, j-1)
            j -= 1

# QUICKSORT
def partition(arr, lo, hi):
    mid = lo + (hi-lo) // 2
    p = arr[mid]
    while True:
        while arr[lo] < p: lo += 1
        while arr[hi] > p: hi -= 1
        if lo >= hi: break
        swap(arr, lo, hi)
        lo += 1
        hi -= 1
    return hi

def __quick(arr, lo, hi):
    if lo >= hi: return
    part = partition(arr, lo, hi)
    __quick(arr, lo, part)
    __quick(arr, part+1, hi)

def quick(arr):
    __quick(arr, 0, len(arr)-1)

# MERGE SORT
def merge_part(arr, lo, mid, hi):
    m_arr = [0] * (hi - lo + 1)
    m_i = 0
    l_i = lo
    r_i = mid + 1
    
    while l_i <= mid and r_i <= hi:
        if arr[l_i] <= arr[r_i]:
            m_arr[m_i] = arr[l_i]
            l_i += 1
        else:
            m_arr[m_i] = arr[r_i]
            r_i += 1
        m_i += 1
    
    while l_i <= mid:
        m_arr[m_i] = arr[l_i]
        l_i += 1
        m_i += 1
    
    while r_i <= hi:
        m_arr[m_i] = arr[r_i]
        r_i += 1
        m_i += 1
    
    for i in range(len(m_arr)):
        arr[lo + i] = m_arr[i]

def __merge(arr, lo, hi):
    if lo >= hi: return
    mid = (lo + hi) // 2
    __merge(arr, lo, mid)
    __merge(arr, mid+1, hi)
    merge_part(arr, lo, mid, hi)

def merge(arr):
    __merge(arr, 0, len(arr)-1)

# NATURAL MERGE SORT
def sorted_run_len(arr, i):
    if i >= len(arr): return 0
    n = 1
    i += 1
    while i < len(arr) and arr[i-1] <= arr[i]:
        n += 1
        i += 1
    return n

def nat_merge(arr):
    i = 0
    while True:
        l_n = sorted_run_len(arr, i)
        if l_n == len(arr): break
        if i+l_n == len(arr):
            i = 0
            continue
        r_n = sorted_run_len(arr, i+l_n)
        merge_part(arr, i, i-1+l_n, i-1+l_n+r_n)
        i = i+l_n+r_n
        if i >= len(arr): i = 0

# BENCHMARKS
size = 5000
if len(sys.argv) > 1:
    try:
        size = int(sys.argv[1])
    except: pass

sorted_data = list(range(size))

nearly_sorted_data = list(range(size))
for _ in range(size//100):
    i, j = random.randint(0, size-1), random.randint(0, size-1)
    nearly_sorted_data[i], nearly_sorted_data[j] = nearly_sorted_data[j], nearly_sorted_data[i]

random_data = [random.randint(1, 10000) for _ in range(size)]

reversed_data = sorted_data.copy()
reversed_data.reverse()

for title, data in {"SORTED": sorted_data, "NEARLY SORTED": nearly_sorted_data, "RANDOM": random_data, "REVERSED": reversed_data}.items():
    print(title)
    data_sorted = sorted(data)
    for func in [selection, insertion, quick, merge, nat_merge]:
        arr = data.copy()
        start = time.time()
        func(arr)
        end = time.time() - start
        print(f"   {func.__name__ + ":":<11} {end:.4f} {"✓" if arr == data_sorted else "𐄂"}")