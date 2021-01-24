import unittest

from browser_compare import *

TESTS_FILE = "browser_compare/tests/test_contents/user-agents-success.txt"


class TestSuccessFullBrowsers(unittest.TestCase):
    def test_successful_updates(self):
        f = open(TESTS_FILE)
        for line in f:
            line = line.split("'")
            a = BrowserCompare(line[1], line[3])
            self.assertTrue(a.compare())

    def test_no_changes(self):
        f = open(TESTS_FILE)
        for line in f:
            line = line.split("'")
            a = BrowserCompare(line[1], line[1])
            self.assertTrue(a.compare())
            a = BrowserCompare(line[3], line[3])
            self.assertTrue(a.compare())

    def test_new_none(self):
        ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:26.0) Gecko/20100101 Firefox/26.0'
        a = BrowserCompare(ua, None)
        with self.assertRaises(UAChangedException) as cm:
            a.compare()

    def test_old_none(self):
        ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:26.0) Gecko/20100101 Firefox/26.0'
        a = BrowserCompare(None, ua)
        with self.assertRaises(UAChangedException) as cm:
            a.compare()

    def test_os_downgrade(self):
        ua_old = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7.1; rv:26.0) Gecko/20100101 Firefox/26.0'
        ua_new = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:26.0) Gecko/20100101 Firefox/26.0'
        a = BrowserCompare(ua_old, ua_new)
        with self.assertRaises(UADowngradedException) as cm:
            a.compare()

    def test_os_main_downgraded(self):
        ua_old = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:26.0) Gecko/20100101 Firefox/26.0'
        ua_new = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:26.0) Gecko/20100101 Firefox/26.0'
        a = BrowserCompare(ua_old, ua_new)
        with self.assertRaises(UADowngradedException) as cm:
            a.compare()

    def test_browser_downgraded(self):
        f = open(TESTS_FILE)
        for line in f:
            line = line.split("'")
            a = BrowserCompare(line[3], line[1])
            with self.assertRaises(UADowngradedException) as cm:
                a.compare()


if __name__ == '__main__':
    unittest.main()
