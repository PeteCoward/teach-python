'''
# TASK 6 - Write a function that takes a string and returns a list containing that string shifted by each integer from 0 to 25
  - use range(0,26) to return a list of integers from 0 to 25 and iterate over them
'''


def get_all_shifts(string):
    ''' returns a list containing all 26 shifts of the input string '''
    raise NotImplementedError


def get_solutions():
    for solution in get_all_shifts('''ILOD IDOL PDL
PDL KDNVRORN KDX
VH ODH, KDX PDWH
VH PDN KDGRPL R
'''):
        print(solution)
