OK_FORMAT = True

test = {   'name': 'q1_3',
    'points': [0, 2],
    'suites': [   {   'cases': [   {   'code': '>>> 1 <= q1_3_percent <= 100\nTrue',
                                       'failure_message': 'Make sure you assign a *percent* to q1_3_percent, not a proportion. Multiply the proportion by 100 to convert it to a percent.',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> q1_3_percent == 100 - q1_2_percent\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
