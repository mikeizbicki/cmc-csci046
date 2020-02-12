import timeit

n = 100

seconds = timeit.timeit(
    'par_checker(xs)',
    'from balanced_parens_2 import par_checker; n='+str(n)+'; xs=n*"["+n*"]"',
    number=1000
    )
print('par_checker takes ',seconds,'seconds')

seconds = timeit.timeit(
    'is_balanced_parens_3(xs)',
    'from balanced_parens import is_balanced_parens_3; n='+str(n)+'; xs=n*"["+n*"]"',
    number=1000
    )
print('is_balanced_parens_3 takes ',seconds,'seconds')

