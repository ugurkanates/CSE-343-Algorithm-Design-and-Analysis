"""


Suppose you have k sorted arrays, each with n elements, and you want to combine them
into a single sorted array that has k x n elements. Propose a divide-and-conquer algorithm for
the problem and implement it with Python.

151044012 Ugurkan ates cse 321

"""

class node:
    def __init__(self, data, row,):
        self.data = data
        self.row = row



def heapmin(heap, i, size):

    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        min_ele = i
        if left < size and heap[min_ele].data > heap[left].data:
            min_ele = left
        if right < size and heap[min_ele].data > heap[right].data:
            min_ele = right

        if min_ele == i:
            break
        else:
            heap[i], heap[min_ele] = heap[min_ele], heap[i]
        i = min_ele


def merge_arrays(matrix, rowm, colm):
    row = rowm
    col = colm
    bubble = [0] * row
    heap = [None] * row
    ans = [None] * (row * col)
    n = row * col
    for i in range(0, row):
        heap[i] = node(matrix[i][0], i)
    for i in range(row - 1, -1, -1):
        heapmin(heap, i, row)
    for i in range(0, n):
        ans[i] = heap[0].data
        mat_row = heap[0].row
        if bubble[mat_row] >= col - 1:
            heap[0] = heap[row - 1]
            row = row - 1
        else:
            bubble[mat_row] += 1
            mat_col = bubble[mat_row]
            heap[0] = node(matrix[mat_row][mat_col], mat_row)
        heapmin(heap, 0, row)


    print("Heres output", ans)


def function():
    matrix = [ [15, 32, 54, 71],
            [2, 43,66, 81],
            [55, 911, 1011, 1123] ]
    merge_arrays(matrix, 3, 4)
function()