OK_FORMAT = True

test = {   'name': 'q3',
    'points': [2, 2, 2, 6],
    'suites': [   {   'cases': [   {'code': ">>> 'Fruit' in fruit_info_caps.columns\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> 'Color' in fruit_info_caps.columns\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> 'Price' in fruit_info_caps.columns\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': '>>> print(fruit_info_caps)\n'
                                               '       Fruit   Color  Price\n'
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
