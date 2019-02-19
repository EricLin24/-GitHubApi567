import unittest
from hw04a_ziangLin import get_github_repo_commit
class TestHw04a(unittest.TestCase):
    def test_unfound_input(self):
        self.assertEqual(get_github_repo_commit(' '), 0,
                         msg="api doesn't find a matched user ID, the return value should be 0")
        self.assertEqual(get_github_repo_commit('=w='), 0,
                         msg="api doesn't find a matched user ID, the return value should be 0")

    def test_request_validation(self):
        self.assertNotEqual(get_github_repo_commit('daseda'), -1,
                            msg="return value shouldn't be -1 or it meets HTTP error")
        self.assertNotEqual(get_github_repo_commit(' '), -1,
                            msg="return value shouldn't be -1 or it meets HTTP error")

    def test_return_type(self):
        self.assertEqual(type(get_github_repo_commit('richkempinski')), list,
                         msg='If enter a valid parameter, it suppose to return a list type value')
        self.assertEqual(type(get_github_repo_commit('richkempinski')[0]), str,
                         msg='Items in the list suppose to be string format')
        self.assertEqual(get_github_repo_commit('richkempinski')[0], 'Repo: hellogitworld Number of commits: 30',
                         msg="The item display should be 'Repo:... Number of commits:...'")
if __name__ == '__main__':
    unittest.main()