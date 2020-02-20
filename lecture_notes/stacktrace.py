'''
Python gives us access to the current stack via the traceback module.
'''

import traceback

def function_a():
    traceback.print_stack()

def function_b():
    function_a()

def function_c():
    function_b()

def function_d():
    function_c()

print('----------------------------------------')
function_a()

print('----------------------------------------')
function_b()

print('----------------------------------------')
function_c()

print('----------------------------------------')
function_d()

print('----------------------------------------')

def recursive(n):
    if n==1:
        traceback.print_stack()
    else:
        recursive(n-1)

recursive(5)
