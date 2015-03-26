'''modual docstrinhg'''
# import cgi
# import platform
import sys
import os
import unittest
# import time
from webapp import library as lib


def main():
    '''function docstring'''
    print('''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Jenkins Test File: ''' + os.path.basename(sys.argv[0]) + '''
**************************************************
Test File(s):
Library.py
''')


class VarsTestCase(unittest.TestCase):
    '''class docstring'''

    def test_HTML_DIR(self):
        '''method docstring'''
        self.assertEqual(lib.HTML_DIR, 'html\\')

    def test_DB_DIR(self):
        '''method docstring'''
        last2 = lib.DB_DIR[-3:]
        first2 = lib.DB_DIR[0:2]
        backandfrount = first2 + last2
        self.assertEqual(backandfrount, 'dbdb\\')

    def test_REDIRECT_DIR(self):
        '''method docstring'''
        self.assertEqual(lib.REDIRECT_DIR, 'redirect\\')

    def test_test(self):
        '''method docstring'''
        self.assertEqual(1, 1)

if __name__ == "__main__":
    main()
    unittest.main()
