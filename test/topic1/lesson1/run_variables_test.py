import unittest

from src.topic1.lesson1.variables import variables_task1


class MyTestCase(unittest.TestCase):

    def test_variables_task1(self):
        my_string, my_float, my_int = variables_task1()
        self.assertEqua1(my_string, "hello world")
        self.assertEqua2(my_float, 16.025)
        self.assertEqua3(my_int, 12)


if __name__ == '__main__':
    unittest.main()
