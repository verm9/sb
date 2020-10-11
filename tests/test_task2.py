from random import randint
import timeit

import knapsack
from pytest import fixture


from functools import wraps

from task2 import knapsack_dp


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = f(*args, **kwargs)
        end = timeit.default_timer()
        print(f'Elapsed time for {f.__name__}: {(end-start)*1e3} ms')
        return result
    return wrapper


@fixture
def generate_random_conditions(num=60, capacity=8000):
    # Generates random incomes, prices and Money that we have.
    prices = [randint(1, 10) for _ in range(num)]
    incomes = [randint(1, 10) for _ in range(num)]
    return {'capacity': capacity, 'prices': prices, 'incomes': incomes}


@timing
def solve_with_dynamic_optimization_lib(data):
    result = knapsack.knapsack(data['prices'], data['incomes']).solve(data['capacity'])
    return result


@timing
def our_implementation(data):
    result = knapsack_dp(data['prices'], data['incomes'], data['capacity'])
    return result


def test_task(generate_random_conditions):
    data = generate_random_conditions

    # Get the lib result.
    lib_result = solve_with_dynamic_optimization_lib(data)

    # Get out result.
    our_result = our_implementation(data)

    assert lib_result == our_result
