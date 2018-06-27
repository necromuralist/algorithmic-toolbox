# python standard library
from datetime import (
    datetime,
    timedelta,
)

MAX_TIME = 5

def time_it(implementation, tag, input_value, expected, max_input, max_time=MAX_TIME):
    """Times the implementation

    Args: 
     implementation: callable to pass input_value to
     tag (str): identifier to add to the output
     input_value (int): the number to pass to the implementation
     expected (int): the expected value
     max_input (int): the largest allowed input value
     max_time (float): number of seconds allowed

    Raises:
        AssertionError: wrong value or took too long
    """
    assert input_value <= max_input, "n too large: {}, max allowed: {}".format(input_value,
                                                                               max_input)
    start = datetime.now()
    print("Starting {}".format(tag))
    actual = implementation(input_value)
    assert actual == expected, "Actual: {} Expected: {}".format(
            actual, expected)
    elapsed = datetime.now() - start
    print("({}) Okay Elapsed time: {}".format(tag, elapsed))
    assert elapsed <= timedelta(seconds=max_time), "Time Greater than {}".format(max_time)
    return

def time_two_inputs(implementation, tag, a_and_b, expected, max_input, max_time=MAX_TIME, allow_timeout=False):
    """Time the implementation

    Args:
     implementation: callable to time
     tag (str): name for the output
     a_and_b (tuple): inputs for the implementation
     expected (int): the expected output of the implementation
     max_input (int): maximum value for a and b
     max_time (float): longest run-time allowed
     allow_timeout (bool): if True, don't raise an exception if it takes too long

    Raises:
     AssertionError: output was wrong or it took too long
    """
    a, b = a_and_b
    assert a <= max_input, "a too large: {}".format(a)
    assert b <= max_input, "b too large: {}".format(b)
    print("Starting {}".format(tag))
    start = datetime.now()
    actual = implementation(a, b)
    elapsed = datetime.now() - start
    print("Elapsed time: {}".format(elapsed))
    assert actual == expected, "Expected: {} Actual: {}".format(expected, actual)
    if not allow_timeout:
        assert elapsed <= timedelta(max_time), "Took too long: {}".format(elapsed)
    return
