import unittest
import reverse

class TestReverseString(unittest.TestCase):
 
    def test_regular_string(self):
        self.assertEqual(reverse("hello"), "olleh")
 
    def test_single_character(self):
        self.assertEqual(reverse("a"), "a")
 
    def test_empty_string(self):
        self.assertEqual(reverse(""), "")
 
    def test_palindrome(self):
        self.assertEqual(reverse("racecar"), "racecar")
 
    def test_spaces(self):
        self.assertEqual(reverse("hello world"), "dlrow olleh")
 
    def test_numbers_in_string(self):
        self.assertEqual(reverse("abc123"), "321cba")
 
    def test_special_characters(self):
        self.assertEqual(reverse("!@#$"), "$#@!")
 
    def test_mixed_case(self):
        self.assertEqual(reverse("HeLLo"), "oLLeH")
 
    def test_two_characters(self):
        self.assertEqual(reverse("ab"), "ba")

if __name__ == "__main__":
    unittest.main()
