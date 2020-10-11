import random
from timeit import default_timer

from pytest import fixture, mark

from task1 import normalize


@fixture
def not_normalized_shares(count=10**6, maximum=10e18):
    return [round(random.uniform(1, maximum), 1) for _ in range(count)]


@mark.parametrize("non_normalized", [[1.5, 3, 6, 1.5]])
@mark.parametrize("normalized", [[0.125, 0.250, 0.500, 0.125]])
def test_normalize(non_normalized, normalized):
    result = normalize(non_normalized)
    assert result == normalized  # Trailing zeros are not counted when compare.


def test_normalize_performance(not_normalized_shares):
    start = default_timer()
    _ = normalize(not_normalized_shares)
    end = default_timer()
    print(f'Elapsed time: {(end-start)*1e3} ms')
