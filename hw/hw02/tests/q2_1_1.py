OK_FORMAT = True

test = {   'name': 'q2_1_1',
    'points': [1, 1, 1],
    'suites': [   {   'cases': [   {   'code': '>>> import numpy as np\n>>> type(interesting_numbers) == np.ndarray\nTrue',
                                       'failure_message': 'Your variable `interesting_numbers` should be a numpy array. See Section 2.1 for instructions on creating an array.',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> len(interesting_numbers)\n4', 'hidden': False, 'locked': False},
                                   {'code': '>>> import numpy as np\n>>> all(interesting_numbers == np.array([0, 1, -1, math.pi]))\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
