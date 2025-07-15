string = "Orange Mango Guava Green Mango Guava Mango Green Apple"

string_arr = string.split()

'''
Mango : 3
Green : 2
Guava : 2
Apple : 1
Orange: 1
'''

print(string_arr)

seen = {}

for ele in string_arr:
    if ele in seen:
        seen[ele] += 1
    else:
        seen[ele] = 1

print(seen)
val = sorted(seen.items())
print(val)


# sorted_items = sorted(freq_map.items(), key=lambda x: (-x[1], x[0]))

# sorted() #sorts this list of tuples.

# '''➡ key=lambda x: (-x[1], x[0])
# 	•	x[1] → frequency
# 	•	-x[1] → sort by frequency descending
# 	•	x[0] → sort by word ascending (if frequencies match)
# '''

# 📝 1️⃣ Start simple: Sort lists

# nums = [5, 2, 9, 1]
# print(sorted(nums))  # ascending
# print(sorted(nums, reverse=True))  # descending


# 📝 2️⃣ Sort list of tuples by one element

# data = [('b', 2), ('a', 3), ('c', 1)]
# print(sorted(data, key=lambda x: x[1]))  # by second item ascending
# print(sorted(data, key=lambda x: -x[1]))  # by second item descending


# ⸻

# 📝 3️⃣ Sort list of tuples by multiple keys

# data = [('b', 2), ('a', 2), ('c', 1)]
# # Descending by number, ascending by letter if tie
# print(sorted(data, key=lambda x: (-x[1], x[0])))
