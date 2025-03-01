from logger_02 import logger


class FlatIterator:

    def __init__(self, list_of_list: list):
        self.list_of_list = list_of_list
        self.start = 0
        self.cursor = -1
        self.len_last_list = len(self.list_of_list[-1])
        self.end = len(self.list_of_list)

    def __iter__(self):
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor >= len(self.list_of_list[self.start]):
            self.start += 1
            self.cursor = 0
            if self.start == self.end:
                raise StopIteration
        item = self.list_of_list[self.start][self.cursor]
        return item


path = 'iter1.log'


@logger(path)
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

        assert flat_iterator_item == check_item, f'\n{flat_iterator_item}\n{check_item}'

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
