OK_FORMAT = True

test = {   'name': 'q6_2_1',
    'points': [1, 1],
    'suites': [   {   'cases': [   {   'code': '>>> import numpy as np\n>>> type(total_charges) == np.ndarray\nTrue',
                                       'failure_message': "It looks like you're not making an array.  You shouldn't need to use .item anywhere in your solution.",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> import numpy as np\n>>> sum(abs(total_charges - np.array([24.144, 47.88, 37.212]))) < 1e-06\nTrue',
                                       'failure_message': "You made an array, but it doesn't have the right numbers in it.",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
