OK_FORMAT = True

test = {   'name': 'q2_1_2',
    'points': [1, 1, 2],
    'suites': [   {   'cases': [   {'code': '>>> type(multiples_of_99) == np.ndarray\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(multiples_of_99)\n102', 'hidden': False, 'locked': False},
                                   {'code': '>>> all(multiples_of_99 == np.arange(0, 9999 + 99, 99))\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
