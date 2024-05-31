import unittest

from calculate import canIBuyBeer


class TestBeer(unittest.TestCase):
    def test_when_17_and_on_krogen_should_not_be_allowed(self):
        # ARRANGE
        age = 17
        loc = "krogen"
        # ACT
        c = canIBuyBeer(age,loc)
        # ASSERT
        #self.assertGreater(990)
        self.assertFalse(c)

    def test_when_18_and_on_krogen_should_be_allowed(self):
        # ARRANGE
        age = 18
        loc = "krogen"
        # ACT
        c = canIBuyBeer(age,loc)
        # ASSERT
        self.assertTrue(c)


    def test_when_20_and_on_systemet_should_be_allowed(self):
        # ARRANGE
        age = 20
        loc = "systemet"
        # ACT
        c = canIBuyBeer(age,loc)
        # ASSERT
        self.assertTrue(c)

    def test_when_19_and_on_systemet_should_not_be_allowed(self):
        # ARRANGE
        age =19
        loc = "systemet"
        # ACT
        c = canIBuyBeer(age,loc)
        # ASSERT
        self.assertFalse(c)

if __name__ == '__main__':
    unittest.main()        