# Входные данные
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

spices = []
sum_b = 0
for ai, bi in zip(a, b):
    spices.append((ai, bi))
    sum_b += bi

# Сортируем по убыванию ai/(ai + bi)
spices.sort(key=lambda x: - (x[0] / (x[0] + x[1])) )

max_value = 0.0
remaining = sum_b

for ai, bi in spices:
    if remaining <= 0:
        break
    s = ai + bi
    if s <= remaining:
        max_value += ai
        remaining -= s
    else:
        fraction = remaining / s
        max_value += fraction * ai
        remaining = 0

print(max_value)