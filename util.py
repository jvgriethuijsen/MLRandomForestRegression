from tinydb import TinyDB

db = TinyDB('matching_platform.json')
teachers_table = db.table('teachers')
schools_table = db.table('schools')
feedback_table = db.table('feedback')