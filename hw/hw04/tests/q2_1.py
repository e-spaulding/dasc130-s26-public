OK_FORMAT = True

test = {   'name': 'q2_1',
    'points': [1, 1, 1, 1],
    'suites': [   {   'cases': [   {'code': '>>> job_titles.num_columns\n2', 'hidden': False, 'locked': False},
                                   {'code': '>>> job_titles.num_rows\n6', 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.asarray(job_titles.labels).item(1) != 'Job full_array'\nTrue",
                                       'failure_message': 'Make sure that you have the correct column labels!',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.asarray(job_titles.labels).item(1) == 'Jobs'\nTrue",
                                       'failure_message': 'Make sure that you have the correct column labels!',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
