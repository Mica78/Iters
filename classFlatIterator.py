class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list

    def __iter__(self):
        self.list_cursor = 0
        self.sublist_cursor = 0
        return self

    def __next__(self):
        if self.list_cursor == len(self.list):
            raise StopIteration
        sublist = self.list[self.list_cursor]
        if self.sublist_cursor < len(sublist):
            item = sublist[self.sublist_cursor]
            self.sublist_cursor += 1
        else:
            self.list_cursor += 1
            self.sublist_cursor = 0
            return self.__next__()
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
