OK_FORMAT = True

test = {   'name': 'q1b',
    'points': [1, 1, 1, 3],
    'suites': [   {   'cases': [   {'code': '>>> fruit_info.shape[1] == 5\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> 'rank2' in fruit_info.columns\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> 1 in fruit_info['rank2'].to_numpy() and 2 in fruit_info['rank2'].to_numpy() and (3 in fruit_info['rank2'].to_numpy()) and (4 in "
                                               "fruit_info['rank2'].to_numpy())\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> np.array_equal(fruit_info['rank1'].to_numpy(), fruit_info['rank2'].to_numpy())\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
