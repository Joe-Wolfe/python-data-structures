
def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a

        >>> number_compare(1, 1)
        'Numbers are equal'

        >>> number_compare(-1, 1)
        'Second is greater'

        >>> number_compare(1, -2)
        'First is greater'
    """
    output = ('Numbers are equal', 'Second is greater', 'First is greater')
    return output[0] if a == b else output[1] if a < b else output[2]
