OK_FORMAT = True

test = {   'name': 'q7_1_5',
    'points': [1, 1],
    'suites': [   {   'cases': [   {'code': '>>> type(farmers_markets_locations_by_latitude) == tables.Table\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> list(np.round(list(farmers_markets_locations_by_latitude.column('y').take(range(3))), 6)) == [64.86275, 64.8459, 64.844414]\nTrue",
                                       'failure_message': 'Check the order of your table.',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
