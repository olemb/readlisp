import pytest
from readlisp import readlisp, LispSymbol

assert readlisp('(a |b|)') == [LispSymbol('a'), LispSymbol('b')]

assert readlisp('(1 2 3 "four")') == [1, 2, 3, "four"]
