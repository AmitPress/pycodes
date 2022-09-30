import gc
for _ in range(100):
    l = [0]
    l.append(l)

print(gc.collect())
print(l)