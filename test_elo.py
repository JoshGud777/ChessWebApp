import cgi
import platform
import sys
import os
import unittest
import time
from webapp import elo as elo


def main():
    print('''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Jenkins Test File: ''' + os.path.basename(sys.argv[0]) + '''
**************************************************
Test File(s):
elo.py
''')


class EstPerTestCase(unittest.TestCase):

    def test_0(self):
        pass
    
    def test_1(self):
        pass

    def test_2(self):
        pass

    def test_3(self):
        pass

    def test_4(self):
        pass
        

class CalPrimesTestCase(unittest.TestCase):

    def test_0(self):
        pass
    
    def test_1(self):
        pass

    def test_2(self):
        pass

    def test_3(self):
        pass

    def test_4(self):
        pass
        

if __name__ == "__main__":
    main()
    unittest.main()
