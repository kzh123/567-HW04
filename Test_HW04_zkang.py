from HW04A_ZKANG import repo
import unittest


class TestHW04(unittest.TestCase):
    def test(self):
        result = ['Repo: hellogitworld Number of commits: 30',
                  'Repo: helloworld Number of commits: 6',
                  'Repo: Mocks Number of commits: 10',
                  'Repo: Project1 Number of commits: 2',
                  'Repo: threads-of-life Number of commits: 1']
        self.assertEqual(repo("richkempinski"), result)


if __name__ == '__main__':
    unittest.main()