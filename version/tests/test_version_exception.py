from version import Version
from nose.tools import raises

class TestVersionException:
    @raises(TypeError)
    def test_eq_should_raise_exception_with_invalid_type(self):
        Version(1.0) == object()

    @raises(TypeError)
    def test_ne_should_raise_exception_with_invalid_type(self):
        Version(1.0) != object()

    @raises(TypeError)
    def test_gt_should_raise_exception_with_invalid_type(self):
        Version(1.0) > object()

    @raises(TypeError)
    def test_ge_should_raise_exception_with_invalid_type(self):
        Version(1.0) >= object()

    @raises(TypeError)
    def test_lt_should_raise_exception_with_invalid_type(self):
        Version(1.0) < object()

    @raises(TypeError)
    def test_le_should_raise_exception_with_invalid_type(self):
        Version(1.0) <= object()