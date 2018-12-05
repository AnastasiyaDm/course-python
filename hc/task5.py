def found_in_dict(one, two):
    result = []
    for i in one:
        for j in two:
            if i == j:
                result.append(i)
    return result


dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_two = {'a': 6, 'b': 7, 'z': 20, 'x': 40}
print(found_in_dict(dict_one, dict_two))
