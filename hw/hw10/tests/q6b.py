OK_FORMAT = True

test = {   'name': 'q6b',
    'points': [5, 5],
    'suites': [   {   'cases': [   {'code': '>>> babynames_2024.shape[0]\n1933', 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.array_equal(just_A_names_2024['First Letter'].to_numpy(), np.array(['A' for _ in range(number_A_babies)]))\nFalse",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
