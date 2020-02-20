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

'''
The output of `python3 stacktrace.py` is:

----------------------------------------
  File "stacktrace.py", line 20, in <module>
    function_a()
  File "stacktrace.py", line 8, in function_a
    traceback.print_stack()
----------------------------------------
  File "stacktrace.py", line 23, in <module>
    function_b()
  File "stacktrace.py", line 11, in function_b
    function_a()
  File "stacktrace.py", line 8, in function_a
    traceback.print_stack()
----------------------------------------
  File "stacktrace.py", line 26, in <module>
    function_c()
  File "stacktrace.py", line 14, in function_c
    function_b()
  File "stacktrace.py", line 11, in function_b
    function_a()
  File "stacktrace.py", line 8, in function_a
    traceback.print_stack()
----------------------------------------
  File "stacktrace.py", line 29, in <module>
    function_d()
  File "stacktrace.py", line 17, in function_d
    function_c()
  File "stacktrace.py", line 14, in function_c
    function_b()
  File "stacktrace.py", line 11, in function_b
    function_a()
  File "stacktrace.py", line 8, in function_a
    traceback.print_stack()
----------------------------------------
  File "stacktrace.py", line 39, in <module>
    recursive(5)
  File "stacktrace.py", line 37, in recursive
    recursive(n-1)
  File "stacktrace.py", line 37, in recursive
    recursive(n-1)
  File "stacktrace.py", line 37, in recursive
    recursive(n-1)
  File "stacktrace.py", line 37, in recursive
    recursive(n-1)
  File "stacktrace.py", line 35, in recursive
    traceback.print_stack()
'''
