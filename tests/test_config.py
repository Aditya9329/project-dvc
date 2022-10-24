import pytest

class NotInRangeError(Exception):
    def __init__(self,msg="value not in range"):
        self.msg    = msg
        super().__init__(self.msg)


def test_generic():
    a = 5
    with pytest.raises(NotInRangeError):
        if a not in range(10,20):
            raise NotInRangeError
    
def test_something():
    a = 2
    b = 2
    assert True