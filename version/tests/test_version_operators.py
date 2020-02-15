from version import Version

class TestVersionOperators:
    def test_v1_should_be_gt_v2(self):
        v1 = Version(2.1)
        v2 = Version(1.8)

        assert v1 > v2
        assert v2 < v1

    def test_v1_should_be_ge_v2(self):
        v1 = Version(2.1)
        v2 = Version(1.8)

        assert v1 >= v2
        assert v2 <= v1

    def test_v1_should_be_gt_n2(self):
        v1 = Version(2.1)

        assert v1 > 1.8
        assert 1.8 < v1
    
    def test_v1_should_be_lt_v2(self):
        v1 = Version(4.1)
        v2 = Version(40.1)

        assert v1 < v2
        assert v2 > v1

    def test_v1_should_be_le_v2(self):
        v1 = Version(4.1)
        v2 = Version(40.1)

        assert v1 <= v2
        assert v2 >= v1

    def test_v1_should_be_lt_n2(self):
        
        assert Version(4.1) < 40.1
        assert 40.1 > Version(4.1)

    def test_v1_minor_version_should_be_lt_n2(self):
        
        assert Version(1.5) < 1.6
        assert 1.6 > Version(1.5)
    
    def test_v1_should_equal_v2(self):
        v1 = Version(1.0)
        v2 = Version(1.0)
        
        assert v1 == v2

    def test_v1_should_equal_n2(self):
        
        assert Version(1.0) == 1.0

    def test_v1_should_not_equal_v2(self):

        assert Version(1.0) != 2.0
    
    def test_version_should_equal_itself(self):
        v1 = Version(10.0)

        assert v1 == v1