import time
from lru_cache import LRUCache
start_time = time.time()


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# cache1 = LRUCache(10000)
# cache2 = LRUCache(10000)
duplicates = []
#
# for i in range(10000):
#     cache1.set(names_1[i], True)
#     cache2.set(names_2[i], True)
#
# for key1 in cache1.keys:
#     if cache2.get(key1):
#         duplicates.append(key1)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

"""
STRETCH GOAL
"""
names_1.sort()
names_2.sort()
n1 = 0
while n1 < len(names_1)-1:
    if names_1[n1] == names_1[n1+1]:
        names_1.pop(n1+1)
    else:
        n1 += 1
n2 = 0
while n2 < len(names_2)-1:
    if names_2[n2] == names_2[n2+1]:
        names_2.pop(n2+1)
    else:
        n2 += 1
all_names = names_1 + names_2
all_names.sort()
for i in range(len(all_names)-1):
    if all_names[i] == all_names[i+1]:
        duplicates.append(all_names[i])
        i += 2



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
