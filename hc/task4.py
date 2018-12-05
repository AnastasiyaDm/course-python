def remove_duplicates(args):
    args.sort()
    i = len(args)-1
    while i > 0:
        if args[i] == args[i-1]:
            del args[i]
        i -= 1
    print(args)


def find_3max(args):
    args.sort()
    print(args[-3:])


def find_min_index(args):
    print(args.index(min(args)))


def reverse_order(args):
    print(args[::-1])


a = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
remove_duplicates(a)
a = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
find_3max(a)
a = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
find_min_index(a)
a = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
reverse_order(a)