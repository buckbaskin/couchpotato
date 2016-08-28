'''
Use property-based testing to verify the correctness of the lazy evaluation
'''
import math

from couchpotato import lazy
from hypothesis import given
from hypothesis.strategies import (text, integers, booleans, floats,
                                   complex_numbers, tuples, characters, binary,
                                   fractions, decimals, one_of)
from nose.tools import assert_equal

def pass_through(value):
    return value

lazy_pass = lazy(pass_through)

@given(one_of(text(), integers(), booleans(),
              floats().filter(lambda x: not math.isnan(x)),
              complex_numbers().filter(lambda x: not math.isnan(x.real) and 
                                       not math.isnan(x.imag)),
              tuples(integers(), integers(),), characters(), binary(),
              fractions(), decimals().filter(lambda x: not math.isnan(x))))
def test_equal_output_text(s):
    assert_equal(pass_through(s), lazy_pass(s))
