def create_dict(args):
    output = {}
    for key in args:
        output[key] = key * key
    return output


keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(create_dict(keys))



