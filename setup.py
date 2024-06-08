import os
import numpy as np
import util

try:
  os.remove("matching_platform.json")
  print(f"File deleted successfully.")
except Exception as e:
  print(f"Exception {e} while removing db")
  
qualifications = ['Bachelors', 'Masters', 'PhD']
subjects = ['Math', 'Science', 'English', 'History']
styles = ['Lecture', 'Interactive', 'Hands-on']
locations = ['New York', 'Boston', 'San Francisco', 'Chicago']
availability = ['Full-time', 'Part-time']
cultures = ['Collaborative', 'Structured', 'Flexible']
requirements = ['Math Teacher', 'Science Teacher', 'English Teacher', 'History Teacher']
salaries = ['40k-50k', '50k-60k', '60k-70k']
demographics = ['Diverse', 'Homogeneous']

# Generate random data
teachers_data = []
for i in range(1, 101):
    teachers_data.append({
        'teacher_id': i,
        'qualifications': np.random.choice(qualifications),
        'experience': np.random.randint(1, 20),
        'subject_expertise': np.random.choice(subjects),
        'teaching_style': np.random.choice(styles),
        'location': np.random.choice(locations),
        'availability': np.random.choice(availability)
    })

schools_data = []
for i in range(1, 51):
    schools_data.append({
        'school_id': i,
        'requirements': np.random.choice(requirements),
        'culture': np.random.choice(cultures),
        'location': np.random.choice(locations),
        'salary_range': np.random.choice(salaries),
        'student_demographics': np.random.choice(demographics)
    })

feedback_data = []
for i in range(1, 201):
    feedback_data.append({
        'teacher_id': np.random.randint(1, 101),
        'school_id': np.random.randint(1, 51),
        'rating': np.random.randint(1, 6)
    })
    
util.teachers_table.insert_multiple(teachers_data)
util.schools_table.insert_multiple(schools_data)
util.feedback_table.insert_multiple(feedback_data)