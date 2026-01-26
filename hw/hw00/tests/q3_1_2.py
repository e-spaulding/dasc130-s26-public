OK_FORMAT = True

test = {   'name': 'q3_1_2',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': ">>> 'seconds_in_a_decade' in vars()\nTrue",
                                       'failure_message': "It looks like you didn't give anything the name seconds_in_a_decade.  Maybe there's a typo, or maybe you just need to run the cell below "
                                                          'Question 3.1.2 where you defined seconds_in_a_decade.',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> seconds_in_a_decade != ...\nTrue',
                                       'failure_message': "It looks like you didn't change the cell to define seconds_in_a_decade appropriately.  It should be a number, computed using Python's "
                                                          'arithmetic.  For example, this is almost right:\n'
                                                          '      seconds_in_a_decade = 10*365*24*60*60',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> seconds_in_a_decade != 315360000\nTrue',
                                       'failure_message': "It looks like you didn't account for leap years. There were 2 leap years and 8 non-leap years in this period. Leap years have 366 days "
                                                          'instead of 365.',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> seconds_in_a_decade == 315532800\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
