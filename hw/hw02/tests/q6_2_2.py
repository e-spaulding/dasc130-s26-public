OK_FORMAT = True

test = {   'name': 'q6_2_2',
    'points': [1, 3],
    'suites': [   {   'cases': [   {   'code': '>>> import numpy as np\n>>> type(more_total_charges) == np.ndarray\nTrue',
                                       'failure_message': "It looks like you're not making an array.  You shouldn't need to use .item anywhere in your solution.",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> import numpy as np\n>>> sum(abs(more_total_charges - 1.2 * more_restaurant_bills)) < 1e-06\nTrue',
                                       'failure_message': "You made an array, but it doesn't have the right numbers in it.",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
