
def get_frequency(num):
    """returns a dictionary that has total frequency of each digit
        >>> get_frequency(1)
        {1: 1}

        >>> get_frequency(12)
        {2: 1, 1: 1}

        >>> get_frequency(121)
        {1: 2, 2: 1}
    """
    frequency_chart = {}
    while (num > 0):
        digit = num % 10
        num //= 10
        frequency_chart[digit] = frequency_chart.get(digit, 0)+1
    return frequency_chart


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    return get_frequency(num1) == get_frequency(num2)
