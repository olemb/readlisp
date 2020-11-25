ReadLisp - Python/Lisp data conversion
=======================================

readlisp provides functions to convert between Lisp expressions and
Python objects, making it easy for Lisp and Python programs to share
data. It is inspired by Mark Probst's Lispreader for C
(http://www.complang.tuwien.ac.at/~schani/lispreader/">Lispreader),
but unlike Lispreader, readlisp converts the Lisp expression into
native Python data types. You can do:

::

    >>> readlisp('(1 2 3 ("Hello" "there"))')
    [1, 2, 3, ['Hello', 'there']]

    >>> writelisp([1, 2, 3.14)])
    '(1 2 3.14)'

Currently, lists, strings, integers, floats and and symbols are
supported. Booleans will probably be supported soon.

Lisp symbols are converted to instances of the LispSymbol class, but
this can be overridden with the optional second argument to
readlisp(). You may pass a dictionary or a function. If you pass a
dictionary, the symbol will be looked up in the dictionary:

::

    >>> readlisp('(a b)', {'a' : 1, 'b' : 2})
    [1, 2]

If you pass a function which takes one argument, the function is
called with the symbol name as an argument and the result is used:

::

    >>> readlisp('(a b)', str)
    ['a', 'b']


Status
-------
    
This is experimental. Anything may change at this point. Comments are
welcome.


Todo
-----

Add unicode support.

What should readlisp() return when there are no more expressions to
read?  It can't return '' or None, since the expression may well be
one of these two. Should it raise an exception?


Ole Martin Bjørndalen - ombdalen@gmail.com
