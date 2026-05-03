OK_FORMAT = True

test = {   'name': 'q5',
    'points': [5, 5, 5, 5],
    'suites': [   {   'cases': [   {'code': '>>> result.shape[0]\n35', 'hidden': False, 'locked': False},
                                   {'code': '>>> result.shape[1]\n5', 'hidden': False, 'locked': False},
                                   {'code': ">>> np.array_equal(np.ones(result.shape[0]) * 2000, result['Year'].to_numpy())\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.greater_equal(result['Count'].to_numpy(), 300).all()\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
