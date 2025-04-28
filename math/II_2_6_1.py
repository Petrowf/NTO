def from_dec_to(n, k):
    nk = []
    while n != 0:
        nk.append(n%k)
        n = n // k
    return nk[::-1]

b = int(input())

N = b**3
cnt = 0
for i in range(N):
    ib = from_dec_to(i, b)
    if len(set(ib)) == 2:
        cnt += 1

print(cnt)