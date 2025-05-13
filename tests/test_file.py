

class TestSuite:
    def test_1(self):
        print("ddd")
        num1 = 2
        assert num1+3 == 2, "Ошибка 1"
        assert 5+5 == 11, "Ошибка 2"

    def test_2(self):
        print("sss")
        assert 5 == 5
        assert 5 < 3
        assert 5 > 3