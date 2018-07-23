import unittest

from main import get_content_by_number


class TestGeneratingContent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.BUFFER = '<buffer>'
        cls.FIFTH_LINE = 'This is every 5th file!'

    def test_fifth_line(self):
        content = get_content_by_number(5, self.BUFFER)
        self.assertEqual(content, self.FIFTH_LINE)

    def test_seventh_line(self):
        content = get_content_by_number(7, self.BUFFER)
        self.assertEqual(content, self.BUFFER)

    def test_divisible_by_five(self):
        pass

    def test_divisible_by_seven(self):
        pass

    def test_divisible_both_by_five_and_seven(self):
        pass

    def test_random_string(self):
        pass

    def test_call_without_buffer(self):
        pass


if __name__ == '__main__':
    unittest.main()
