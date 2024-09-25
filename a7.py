# CS305 Park University
# Assignment #7 Solution Code
# Datalog
# By Cyrille Tekam Tiako
# 25 Sep 2024

from pyDatalog import pyDatalog

# Initialize pyDatalog and define necessary terms
pyDatalog.create_terms('subject, completed, graduated, load_course_catalog, assert_student_completed_class, load_graduation_rules, ask_if_graduated, find_graduates')

# 1. Load course catalog with subjects
def load_course_catalog():
    """Asserts all knowledge of classes and their respective subjects."""
    # Assert courses and their respective subjects
    subject('cs101', 'STEM')
    subject('mat167', 'STEM')
    subject('art310', 'Humanities')
    subject('eng101', 'Humanities')
    subject('his110', 'Social Science')
    subject('psy150', 'Social Science')

# 2. Assert that a student has completed a specified course
def assert_student_completed_class(studentid, courseid):
    """Asserts that the specified student has completed the specified course."""
    completed(studentid, courseid)

# 3. Load graduation rules to determine if a student has graduated
def load_graduation_rules():
    """Loads rules for determining if a student has graduated."""
    # A student graduates if they have completed at least one course from each subject
    pyDatalog.load("""
    graduated(Student) <- completed(Student, Course) & subject(Course, Subject) &
                           (Subject == 'STEM' | Subject == 'Humanities' | Subject == 'Social Science')
    """)

# 4. Determine if the given student has graduated
def ask_if_graduated(studentid):
    """Determines if the given student has graduated or not."""
    return graduated(studentid)

# 5. Find all graduating students
def find_graduates():
    """Returns a set of all students who have graduated."""
    res = set()
    ans = pyDatalog.ask("graduated(X)")
    if ans:
        for t in ans.answers:
            res.add(t[0])
    return res

def main():
    # Student course completions for various students
    assert_student_completed_class('s001', 'psy150')  # Completed Social Science
    assert_student_completed_class('s001', 'eng101')   # Completed Humanities
    assert_student_completed_class('s001', 'mat167')   # Completed STEM
    assert_student_completed_class('s001', 'cs101')    # Completed STEM

    assert_student_completed_class('s002', 'psy150')   # Completed Social Science
    assert_student_completed_class('s002', 'his110')   # Completed Social Science
    assert_student_completed_class('s002', 'cs101')    # Completed STEM
    assert_student_completed_class('s002', 'mat167')   # Completed STEM

    assert_student_completed_class('s003', 'art310')   # Completed Humanities
    assert_student_completed_class('s003', 'eng101')    # Completed Humanities

    assert_student_completed_class('s004', 'his110')   # Completed Social Science
    assert_student_completed_class('s004', 'psy150')   # Completed Social Science
    assert_student_completed_class('s004', 'cs101')    # Completed STEM
    assert_student_completed_class('s004', 'mat167')   # Completed STEM

    # Load course catalog and graduation rules
    load_course_catalog()
    load_graduation_rules()

    # Check graduation status for students
    print('Student s001 did ' +
          ('' if ask_if_graduated('s001') else 'not ') +
          'graduate.')
    
    print('Student s002 did ' +
          ('' if ask_if_graduated('s002') else 'not ') +
          'graduate.')
    
    print('Student s003 did ' +
          ('' if ask_if_graduated('s003') else 'not ') +
          'graduate.')
    
    print('Student s004 did ' +
          ('' if ask_if_graduated('s004') else 'not ') +
          'graduate.')

    # List graduating students
    print('Graduating students:', find_graduates())

if __name__ == '__main__':
    main()
