import pytest
from readlisp import readlisp, LispSymbol

assert readlisp('(a |b|)') == [LispSymbol('a'), LispSymbol('b')]

assert readlisp('(1 2 3 "four")') == [1, 2, 3, "four"]

# TODO: How do we handle these cases? (And what does this mean?)
# assert readlisp("(a '|b|)") == ?
# assert readlisp("(a :|b|)") == ?

