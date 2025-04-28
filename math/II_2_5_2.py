import itertools

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
unique = []

shashlyk = "Б"*a + "К"*b + "А"*c + "М"*d
print(shashlyk)
permutations = itertools.permutations(shashlyk)
for p in permutations:
    if p not in unique:
        unique.append(p)

print(len(unique))