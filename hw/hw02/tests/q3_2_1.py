OK_FORMAT = True

test = {   'name': 'q3_2_1',
    'points': [1, 1],
    'suites': [   {   'cases': [   {   'code': '>>> import numpy as np\n>>> type(population_rounded) == np.ndarray\nTrue',
                                       'failure_message': "It looks like you're not making an array.  You shouldn't need to use .item anywhere in your solution.",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> import numpy as np\n>>> sum(population_rounded) == 312868000000\nTrue',
                                       'failure_message': "You made an array, but it doesn't have the right numbers in it.",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
