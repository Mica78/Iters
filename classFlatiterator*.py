"""
*Необязательное задание.Написать итератор, аналогичный итератору из задания 1,
но обрабатывающий списки с любым уровнем вложенности.Шаблон и тест в коде ниже:
"""


class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list
        self.stack = []

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor >= len(self.list):
            if not self.stack:
                raise StopIteration
            else:
                self.list, self.cursor = self.stack.pop()
                return self.__next__()

        self.item = self.list[self.cursor]
        self.cursor += 1
        if not isinstance(self.item, list):
            return self.item
        else:
            self.stack.append((self.list, self.cursor))
            self.list = self.item
            self.cursor = 0
            return self.__next__()


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()

