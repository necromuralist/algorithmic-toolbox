MAX_TIME = 5

def time_it(implementation, tag, input_value, expected, max_time=MAX_TIME, max_input=MAX_INPUT):
    """Times the implementation

    Args: 
     implementation: callable to pass input_value to
     tag (str): identifier to add to the output
     input_value (int): the number to pass to the implementation
     expected (int): the expected value
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
    assert elapsed <= max_time, "Time Greater than {}".format(max_time)
    return
