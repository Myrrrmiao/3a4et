class FlattenIterator:

    def __init__(self, nested_list):
        self.iterators = [iter(nested_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.iterators:
            try:
                item = next(self.iterators[-1])
            except StopIteration:
                self.iterators.pop()
                continue

            if isinstance(item, list):
                self.iterators.append(iter(item))
                continue

            return item

        raise StopIteration
# Пример
nested_list = [1, [2, [3, 4], 5], 6]
for num in FlattenIterator(nested_list):
    print(num)
