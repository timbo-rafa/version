from version import Version

class TestVersion:
    def test_different_formats_should_be_equal(self):
        v1 = Version(2)
        v2 = Version("2")
        v3 = Version(2.000000)
        v4 = Version("v0002.0.000000")

        assert v1 == v2 == v3 == v4

    def test_major(self):
        v1 = Version("11.0.0")
        v2 = Version("12.0.0")
        v3 = Version("v11.99.99rc99")

        assert v2 > v1
        assert v2 > v3
    
    def test_minor(self):
        v1 = Version("v22.0.0")
        v2 = Version("v22.1.0")
        v3 = Version("v22.0.9")

        assert v2 > v1
        assert v2 > v3

    def test_patch(self):
        v1 = Version("v11.11.19")
        v2 = Version("v11.11.2")
        v3 = Version("v11.11.09")

        assert v1 > v2
        assert v1 > v3

    def test_alpha_should_be_lt_beta(self):
        v1 = Version("1.0.0a")
        v2 = Version("1.0.0b")

        assert v1 < v2
    
    def test_beta_should_be_lt_rc(self):
        v1 = Version("1.0.0b")
        v2 = Version("1.0.0rc")

        assert v1 < v2
    
    def test_rc_should_be_lt_no_candidate(self):
        v1 = Version("1.0.0rc")
        v2 = Version("1.0.0")

        assert v1 < v2

    def test_beta_versions(self):
        v1 = Version("2b10")
        v2 = Version("2b11")

        assert v1 < v2
    
    def test_tricky(self):
        v1 = Version("1.9")
        v2 = Version("1.10")

        assert v2 > v1