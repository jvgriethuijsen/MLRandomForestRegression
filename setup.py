import os, util
import numpy as np

util.teachers_table.truncate()
util.schools_table.truncate()
util.feedback_table.truncate()

qualifications = ['Bachelors', 'Masters', 'PhD']
subjects = ['Math', 'Science', 'English', 'History']
styles = ['Lecture', 'Interactive', 'Hands-on']
locations = ['Amsterdam', 'Rotterdam', 'The Hague', 'Utrecht', 'Eindhoven']
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

# Generate feedback based on meaningful matches
feedback_data = []
for teacher in teachers_data:
    for school in schools_data:
        
        if (teacher['subject_expertise'] + ' Teacher' == school['requirements'] and teacher['location'] == school['location']):
            rating = np.random.randint(4, 6) # Excellent match: subject and location align
            print(f"Teacher from {teacher['location']} with expertise {teacher['subject_expertise']} was an excellent match ({rating})")
        
        elif teacher['subject_expertise'] + ' Teacher' == school['requirements']:
            rating = np.random.randint(3, 5)  # Partial match: only subject aligns
        
        else:
            rating = np.random.randint(1, 3)  # No match: neither subject nor location aligns
        
        feedback_data.append({
            'teacher_id': teacher['teacher_id'],
            'school_id': school['school_id'],
            'rating': rating
        })
    
util.teachers_table.insert_multiple(teachers_data)
util.schools_table.insert_multiple(schools_data)
util.feedback_table.insert_multiple(feedback_data)