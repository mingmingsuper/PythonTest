import unittest

from Student import Student


class TestStudent(unittest.TestCase):

    def test_score(self):
        student = Student('java', 10, 20)
        self.assertGreaterEqual(student.score, 0, 'score must be larger than zero')

    def test_name(self):
        student = Student('java', 10, 20)
        self.assertEqual(student.name, 'java', 'name is not java')

    def test_age(self):
        student = Student('java', 10, 20)
        self.assertGreaterEqual(student.age, 0, 'age must be larger than zero')


# if __name__ == '__main__':
#     unittest.main()
