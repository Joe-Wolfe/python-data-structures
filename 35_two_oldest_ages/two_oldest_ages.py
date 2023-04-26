import doctest


def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([5, 5, 2, 5])
        (2, 5)
    """
    start = 1
    while (ages[0] == ages[start]):
        start += 1
    second_oldest = min(ages[0], ages[start])
    oldest = max(ages[0], ages[start])

    for index in range(start+1, len(ages)):
        new_age = ages[index]
        if (new_age == oldest):
            continue
        if (new_age > oldest):
            second_oldest = oldest
            oldest = new_age
        elif (new_age > second_oldest):
            second_oldest = new_age
    return (second_oldest, oldest)


doctest.testmod()
