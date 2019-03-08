import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

dups = {}

duplicates = []
for name_1 in names_1:
    if name_1 not in dups:
        dups[name_1] = 0
    dups[name_1] += 1

for name_2 in names_2:
    if name_2 in dups:
        duplicates.append(name_2)

# check for dups in names 1 returns false
# for x in dups:
#     if dups[x] > 1:
#         print(True)
#     else:
#         print(False)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
