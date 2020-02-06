import timeit

seconds = timeit.timeit(
    'is_balanced_parens_3(xs)',
    'from balanced_parens import is_balanced_parens_3; n=1000; xs=n*"["+n*"]"',
    number=1000
    )
print('seconds=',seconds)
