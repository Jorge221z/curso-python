import os
os.system("clear")

"""
Dado un array de números y un número goal, 
encuentra los dos primeros números del array que sumen el número goal y 
devuelve sus índices. 
Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""


# def find_first_sum(nums, goal):
#     suma = 0
#     for i in nums:
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == goal:
#                 return [i, j]
            
#     return None


def find_first_sum(nums, goals):
    seen = {} #guardamos numero y su indice

    for index, value in enumerate(nums):
        missing = goal - value
        if missing in seen: return[seen[missing], index]
        seen[value] = index

    return None

nums = [4, 5, 6, 2]
goal = 8

result = find_first_sum(nums, goal)  # [2, 3]
print(result)