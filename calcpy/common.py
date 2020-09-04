from collections import deque
from collections import defaultdict


def level_traversal(tree, callback = lambda level, shape, value: None):
    q = deque()
    q.append((0, tree))
    q_len = len(q)

    while q:
        level, item = q.popleft()
        n_level = level + 1
        try:
            q.extend((n_level, x) for x in item)
            iterable_flag = 1
        except TypeError:
            yield item
            iterable_flag = 0
        shape = -q_len + iterable_flag + (q_len:=len(q))
        callback(level, shape, item)


# TODO: move testing to standalone test suite

import pytest


@pytest.mark.parametrize("input, expected_dict, expected_list", [
        ([1,2,3], {0:[3], 1:[-1]*3}, [1,2,3]),
        ([[1,2,3]], {0:[1], 1:[3], 2:[-1]*3}, [1,2,3]),
        ([[]], {0:[0]}, []),
        ([], {}, []),
        (1, {0:[-1]}, [1]),
        ([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]], {0:[2]*1, 1:[2]*2, 2:[3]*4, 3:[-1]*12}, [1,2,3,4,5,6,7,8,9,10,11,12]),
    ])
def test_ltt(input, expected_dict, expected_list):
    dd = defaultdict(list)
    callback = lambda level, shape, value: dd[level].append(shape)
    assert list(level_traversal(input, callback)) == expected_list
    assert dd == expected_dict
