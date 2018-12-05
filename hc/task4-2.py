class Task:
    def __init__(self):
        self.args = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

    def remove_duplicates(self):
        self.args.sort()
        i = len(self.args) - 1
        while i > 0:
            if self.args[i] == self.args[i - 1]:
                del self.args[i]
            i -= 1
        print(self.args)

    def find_3max(self):
        self.args.sort()
        print(self.args[-3:])

    def find_min_index(self):
        print(self.args.index(min(self.args)))

    def reverse_order(self):
        print(self.args[::-1])


task1 = Task()
task2 = Task()
task3 = Task()
task4 = Task()
task1.remove_duplicates()
task2.find_3max()
task3.find_min_index()
task4.reverse_order()
