"""lab 7
    Brooke
    4/4/18"""
def all_greetings_greater_3(greeting_histogram):
    """
        This function reduces a histogram by totaling the greetings that we use.
        greeting_histogram: dictionary with greeting strings as keys and
        frequencies as values.
        returns: interger: sum of frequencies of values

        all_greetings_greater_3('hi':5, 'bye': 10, 'hola':23, 'good morning':0)
    """
    total = 0
    greeting_histogram = {'hi':5, 'bye': 10, 'hola':23, 'good morning':0}
    for k in greeting_histogram:
        if len(k)> 3:
            total = total + greeting_histogram[k]
    return total

    if __name__ == '__main__':
        import doctest
        doctest.testnow()
