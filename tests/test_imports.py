'''
Test that the import structure of the couchpotato exposes the correct items
'''
from nose.tools import assert_in, assert_not_in, assert_is_instance, assert_raises

def test_available():
    import couchpotato
    assert_in('lazy', dir(couchpotato))

def test_not_available():
    import couchpotato
    for item in ['very', 'lazify', 'Lazy']:
        assert_not_in(item, dir(couchpotato))

def test_not_couchpotato_very():
    import couchpotato.very
    with assert_raises(AttributeError):
        dir(couchpotato.very)

def test_not_very_lazy():
    import couchpotato.very.lazy
    with assert_raises(AttributeError):
        dir(couchpotato.very.lazy)

def test_Lazy_exteded():
    from couchpotato.very.lazy import Lazy
    assert_is_instance(Lazy(lambda x: x, (), {}), Lazy)

