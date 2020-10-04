from heap import Heap


def to_heap(arr):
    heap = Heap()
    for item in arr:
        heap.insert(item)
    return heap


def get_sorted_arr(heap):
    lst = []
    while heap.size:
        lst.append(heap.extract_min())
    return lst


def to_heap_fast(arr):
    heap = Heap()
    heap.values = arr[:]
    heap.sift_up = len(arr)
    for i in reversed(range(n//2)):
        heap.sift_down(i)
    return heap
