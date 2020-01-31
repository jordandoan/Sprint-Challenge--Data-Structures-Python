import time
from lru_cache import LRUCache
from bst import BinarySearchTree
start_time = time.time()


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

root1 = BinarySearchTree(names_1[0])
root2 = BinarySearchTree(names_2[0])
for i in range(1, 10000):
    root1.insert(names_1[i])
    root2.insert(names_2[i])

def findDupes(node1, root2, ans):
    if not node1:
        return
    if root2.contains(node1.value):
        ans.append(node1.value)
    findDupes(node1.left, root2, ans)
    findDupes(node1.right, root2, ans)
    return ans

# cache1 = LRUCache(10000)
# cache2 = LRUCache(10000)
duplicates = []
findDupes(root1, root2, duplicates)

# print(duplicates)
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
# names_1.sort()
# names_2.sort()
# n1 = 0
# while n1 < len(names_1)-1:
#     if names_1[n1] == names_1[n1+1]:
#         names_1.pop(n1+1)
#     else:
#         n1 += 1
# n2 = 0
# while n2 < len(names_2)-1:
#     if names_2[n2] == names_2[n2+1]:
#         names_2.pop(n2+1)
#     else:
#         n2 += 1
# all_names = names_1 + names_2
# all_names.sort()
# for i in range(len(all_names)-1):
#     if all_names[i] == all_names[i+1]:
#         duplicates.append(all_names[i])
#         i += 2



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
