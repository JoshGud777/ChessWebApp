import cgi
import platform
import sys
import os
import unittest
import time
from webapp import library as lib
from webapp import login as log


def main():
    print('''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Jenkins Test File: ''' + os.path.basename(sys.argv[0]) + '''
**************************************************
Test File(s):
Library.py
''')


class VarsTestCase(unittest.TestCase):

    def test_HTML_DIR(self):
        self.assertEqual(lib.HTML_DIR, 'html\\')
        pass

    def test_DB_DIR(self):
        last2 = lib.DB_DIR[-3:]
        first2 = lib.DB_DIR[0:2]
        backandfrount = first2 + last2
        self.assertEqual(backandfrount, 'dbdb\\')

    def test_REDIRECT_DIR(self):
        self.assertEqual(lib.REDIRECT_DIR, 'redirect\\')

    def test_test(self):
        self.assertEqual(1, 1)

if __name__ == "__main__":
    main()
    time.sleep(1)
    unittest.main()
