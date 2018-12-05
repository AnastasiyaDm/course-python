def create_list(args):
    output = []
    for i in args:
        if i % 2 == 0:
            output.append(i)
    return output


numbers = [i for i in range(0, 101)]
print(create_list(numbers))

