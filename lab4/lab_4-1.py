import array

def compute_min_sum(input_file):
    with open(input_file, 'r') as f:
        data = f.read().split()

    n, k = int(data[0]), int(data[1])
    arr = array.array('i', map(int, data[2:2+n]))


    prefix_min = array.array('i', [0] * n)
    current_min = arr[0]
    prefix_min[0] = current_min
    for i in range(1, n):
        if arr[i] < current_min:
            current_min = arr[i]
        prefix_min[i] = current_min


    suffix_min = array.array('i', arr)
    current_min = suffix_min[-1]
    for i in range(n-2, -1, -1):
        if suffix_min[i] < current_min:
            current_min = suffix_min[i]
        else:
            suffix_min[i] = current_min


    min_sum = float('inf')
    start_j = k
    end_j = n - k - 1

    if start_j > end_j:
        return -1

    for j in range(start_j, end_j + 1):
        a = prefix_min[j - k]
        c = suffix_min[j + k]
        current_sum = a + arr[j] + c
        if current_sum < min_sum:
            min_sum = current_sum

    return min_sum


print(compute_min_sum('27-165a.txt'))
print(compute_min_sum('27-165b.txt'))