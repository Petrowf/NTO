def holodilniki(a, b):
    N = 280
    while True:
        if N%5 == 0 and (N - a)%7 == 0 and (N - b)%8 == 0:
            return N
        else:
            N += 1

a = int(input("a: "))
b = int(input("b: "))
N = int(holodilniki(a, b))
print(N)