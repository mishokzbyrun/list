#2
# dict1 = {input()}
# dict2 = {input()}
# if dict1.symmetric(dict2):
#     list1 = dict1.update(dict2)
#     print(list1)
# else:
#     print("no symetry")

#3
# unique_dict = {"a","b","c","d"}

# not_unique_dict = {}

# for key, value in unique_dict.items():
#     if value not in not_unique_dict:
#         not_unique_dict[value] = []

#     not_unique_dict[value].append(key)


# print(not_unique_dict)
# for key, value in not_unique_dict.items():
#     print(f"{key}: {value}")

#4
# dict1 = {"b","d","h","a","f","g","e","c"}
# sorted_dict = {key: dict1[key] for key in sorted(dict1)}
# print(sorted_dict)

#5
# my_dict = {"apple":"pay","google":"play","visual":"studio"}
# search = "search"
# keys = []


# for key, value in my_dict.items():

#     if isinstance(value, str) and search in value:

#         keys.append(key)
# print(keys)

#6
# tuple_list = [(1, 'aple'), (2, 'google'), (3, 'redmi')(4, "IBM")]
# result_dict = dict(tuple_list)

# print(result_dict)

#7
# tuple_list = [(1, 'aple'), (2, 'booknet'), (1, 'chrome')]
# result_dict = {}

# for key, value in tuple_list:
#     if key in result_dict:
#         result_dict[key].append(value)
#     else:
#         result_dict[key] = [value]

# print(result_dict)

#8
# dict1 = {'a': [1, 2], 'b': [3, 4]}
# dict2 = {'a': [5], 'b': [6, 7]}
# dict3 = {}

# for key in set(dict1.keys()).union(set(dict2.keys())):
#     dict3[key] = dict1.get(key, []) + dict2.get(key, [])

# print(dict3)

#9
# my_dict = {'a': 5, 'b': 5, 'c': 40, 'd': 12, 'e': 92}

# max_key = max(my_dict, key=my_dict.get)

# min_key = min(my_dict, key=my_dict.get)

# print(my_dict)
# print(f"max: {max_key} = {my_dict[max_key]})")
# print(f"min {min_key} = {my_dict[min_key]})")

#10
dict1 = {'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}}
total_sum = 0

for key1, dict2 in dict1.items():
    for key2, value in dict2.items():
        if isinstance(value, int):
            total_sum += value

print(total_sum)