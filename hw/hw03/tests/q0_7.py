OK_FORMAT = True

test = {   'name': 'q0_7',
    'points': [0, 2, 3],
    'suites': [   {   'cases': [   {   'code': '>>> remaining_inventory.num_columns\n3',
                                       'failure_message': "It looks like your table doesn't have all 3 columns that are in the inventory table.",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> remaining_inventory.column('count').item(0) != 45\nTrue",
                                       'failure_message': 'It looks like you forgot to subtract off the sales.',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> remaining_inventory.where(1, 'grape')\nbox ID | fruit name | count\n57930  | grape      | 162", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
