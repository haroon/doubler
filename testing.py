import unittest
from collections import namedtuple
from doubler import marching_doubler, out_file

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(Tests, cls).setUpClass()

        test_fixture = namedtuple('test_fixture', 'rl sl expected')

        fix1 = test_fixture(4, 16, '1,1,2,3,1,2,2,3,1,2,3,3,1,1,2,3,')
        fix2 = test_fixture(4, 15, '1,1,2,3,1,2,2,3,1,2,3,3,1,1,2,')
        fix3 = test_fixture(4, 32, '1,1,2,3,1,2,2,3,1,2,3,3,1,1,2,3,1,2,2,3,1,2,3,3,1,1,2,3,1,2,2,3,')
        fix4 = test_fixture(4, 30, '1,1,2,3,1,2,2,3,1,2,3,3,1,1,2,3,1,2,2,3,1,2,3,3,1,1,2,3,1,2,')
        fix5 = test_fixture(5, 16, '1,1,2,3,4,1,2,2,3,4,1,2,3,3,4,1,')
        fix6 = test_fixture(5, 17, '1,1,2,3,4,1,2,2,3,4,1,2,3,3,4,1,2,')
        fix6 = test_fixture(5, 20, '1,1,2,3,4,1,2,2,3,4,1,2,3,3,4,1,2,3,4,4,')
        fix7 = test_fixture(7, 5, '1,1,2,3,4,')
        fix8 = test_fixture(1, 1, '')
        fix9 = test_fixture(1, 4, '')
        fix10 = test_fixture(-1, 10, '')
        fix11 = test_fixture(5, -1, '')
        fix12 = test_fixture(4, 1, '1,')
        fix13 = test_fixture(3, 0, '')
        fix14 = test_fixture(0, 0, '')
        fix15 = test_fixture(10, 7, '1,1,2,3,4,5,6,')

        cls.fixtures = [fix1, fix2, fix3, fix4, fix5, fix6, fix7, fix8, fix9, fix10, fix11, fix12, fix13, fix14, fix15]

    def test_marching_doubler(self):
        for fixture in self.fixtures:
            self._verify_result(fixture)

    def _verify_result(self, fixture):
        marching_doubler(fixture.rl, fixture.sl)
        with open(out_file, 'r+') as results:
            res = results.readline()
            self.assertEqual(res, fixture.expected, f'Expecting {fixture.expected} but found {res} with run length: {fixture.rl} and sequence length: {fixture.sl}')
            results.truncate(0)

if __name__ == '__main__':
    unittest.main()
