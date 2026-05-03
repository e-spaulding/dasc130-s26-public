OK_FORMAT = True

test = {   'name': 'q1a',
    'points': [1, 1, 2],
    'suites': [   {   'cases': [   {'code': '>>> fruit_info.shape[1] == 4\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> 'rank1' in fruit_info.columns\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> 1 in fruit_info['rank1'].to_numpy() and 2 in fruit_info['rank1'].to_numpy() and (3 in fruit_info['rank1'].to_numpy()) and (4 in "
                                               "fruit_info['rank1'].to_numpy())\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
