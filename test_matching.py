import unittest
from matching_model import predict_match


class TestMatchPrediction(unittest.TestCase):

    def test_perfect_match(self):
        teacher_profile = {
            'qualifications': 'Masters',
            'experience': 10,
            'subject_expertise': 'Math',
            'teaching_style': 'Interactive',
            'location': 'Amsterdam',
            'availability': 'Full-time'
        }
        school_profile = {
            'requirements': 'Math Teacher',
            'culture': 'Collaborative',
            'location': 'Amsterdam',
            'salary_range': '50k-60k',
            'student_demographics': 'Diverse'
        }
        predicted_rating = predict_match(teacher_profile, school_profile)
        print(f"Perfect match predicted rating: {predicted_rating}")
        self.assertTrue(4 <= predicted_rating <= 5, f"Expected rating between 4 and 5, got {predicted_rating}")


    def test_partial_match(self):
        teacher_profile = {
            'qualifications': 'Masters',
            'experience': 10,
            'subject_expertise': 'Math',
            'teaching_style': 'Interactive',
            'location': 'Rotterdam',
            'availability': 'Full-time'
        }
        school_profile = {
            'requirements': 'Math Teacher',
            'culture': 'Collaborative',
            'location': 'Amsterdam',
            'salary_range': '50k-60k',
            'student_demographics': 'Diverse'
        }
        predicted_rating = predict_match(teacher_profile, school_profile)
        print(f"Partial match predicted rating: {predicted_rating}")
        self.assertTrue(3 <= predicted_rating <= 4, f"Expected rating between 3 and 4, got {predicted_rating}")


    def test_poor_match(self):
        teacher_profile = {
            'qualifications': 'Masters',
            'experience': 10,
            'subject_expertise': 'History',
            'teaching_style': 'Interactive',
            'location': 'Rotterdam',
            'availability': 'Full-time'
        }
        school_profile = {
            'requirements': 'Math Teacher',
            'culture': 'Collaborative',
            'location': 'Amsterdam',
            'salary_range': '50k-60k',
            'student_demographics': 'Diverse'
        }
        predicted_rating = predict_match(teacher_profile, school_profile)
        print(f"Poor match predicted rating: {predicted_rating}")
        self.assertTrue(1 <= predicted_rating <= 2, f"Expected rating between 1 and 2, got {predicted_rating}")


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)