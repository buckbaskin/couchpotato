'''
The couchpotato module is used to lazily evaluate functions.

The external interface is:
from couchpotato.decorator import lazy

@lazy
def your_function():
   ...

'''

# make sure Lazy is imported, but don't expose it as couchpotato.Lazy
from couchpotato.very.lazy import Lazy
del Lazy

# rename lazify to lazy externally
# the decorator is:
# @lazy
# def function():
from couchpotato.decorator import lazy

# don't expose the decorator module, just its lazy/lazify decorator
del decorator

# don't expose very, just from couchpotato.very.lazy import Lazy
del very
