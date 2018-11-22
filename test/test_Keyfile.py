import unittest
import Keyfile

class TestKeyfile(unittest.TestCase):
    def test_write_line(self):
        k = Keyfile.Keyfile("some/path")
        k.write_line("blablabla-line1")
        #TODO How to unit test that? Which assert to test?? Shouldn't write_line return something?

if __name__ == '__main__':
    unittest.main()