OK_FORMAT = True

test = {   'name': 'q2',
    'points': [2, 2, 2, 6],
    'suites': [   {   'cases': [   {'code': '>>> fruit_info.shape[1] == 3\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> 'rank1' not in fruit_info.columns\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> 'rank2' not in fruit_info.columns\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': '>>> print(fruit_info)\n'
                                               '       fruit   color  price\n'
                                               '0      apple     red   1.00\n'
                                               '1     orange  orange   0.75\n'
                                               '2     banana  yellow   0.35\n'
                                               '3  raspberry    pink   0.05\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
