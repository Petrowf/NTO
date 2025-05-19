n, m, k = map(int, input().split())
requests = list(map(int, input().split()))

ann = [[0 for j in range(m)] for i in range(n)]
yan = [[0 for j in range(m)] for i in range(n)]
times = [[0 for j in range(m)] for i in range(n)]
# Анна
ann_time = 1
ann_i = 0
ann_j = m - 1
mode = 0
circle = 0
while ann_time <= n*m:
    if mode == 0:
        ann[ann_i][ann_j] = ann_time
        ann_time += 1
        ann_i += 1
        if ann_i > n - 1 - circle:
            mode = 1
            ann_i = n - 1 - circle
            ann_j -= 1
    elif mode == 1:
        ann[ann_i][ann_j] = ann_time
        ann_time += 1
        ann_j -= 1
        if ann_j < 0 + circle:
            mode = 2
            ann_j = 0 + circle
            ann_i -= 1
    elif mode == 2:
        ann[ann_i][ann_j] = ann_time
        ann_time += 1
        ann_i -= 1
        if ann_i < 0 + circle:
            mode = 3
            ann_i = 0 + circle
            ann_j += 1
            circle += 1
    else:
        ann[ann_i][ann_j] = ann_time
        ann_time += 1
        ann_j += 1
        if ann_j > m - 1 - circle:
            mode = 0
            ann_j = m - 1 - circle
            ann_i += 1


yan_time = 1
yan_i = 0
yan_j = m-1
mode = 0
while yan_time <= n*m:
    yan[yan_i][yan_j] = yan_time
    yan_time += 1
    if mode == 0:
        if yan_j == 0:
            yan_i += 1
            mode = 1
        else:
            yan_j -= 1
    else:
        if yan_j == m - 1:
            yan_i += 1
            mode = 0
        else:
            yan_j += 1

for i in range(n):
    for j in range(m):
        times[i][j] = max(ann[i][j], yan[i][j])


answers = []
for req in requests:






