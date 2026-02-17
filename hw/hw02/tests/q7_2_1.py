OK_FORMAT = True

test = {   'name': 'q7_2_1',
    'points': [1, 1, 1],
    'suites': [   {   'cases': [   {'code': '>>> type(above_eight) == tables.Table\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> above_eight.num_rows == 20\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> print(above_eight.sort(0).take([17]))\nTitle       | Rating\nToy Story 3 | 8.3\n',
                                       'failure_message': 'Make sure your columns are in the right order! First column should be Title, second column should be Rating',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
