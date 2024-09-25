# CS305 Park University
# Assignment #7 Solution Code
# Datalog
# By Cyrille Tekam Tiako
# 25 Sep 2024

from pyDatalog import pyDatalog

# Load the Datalog environment
pyDatalog.create_terms('student_completed, subject, completed, graduated, ask_if_graduated')

# 1.
def load_course_catalog():
    """Asserts all knowledge of classes and their subjects."""
    +subject('cs101', 'STEM')
    +subject('mat167', 'STEM')
    +subject('art310', 'Humanities')
    +subject('eng101', 'Humanities')
    +subject('his110', 'Social Science')
    +subject('psy150', 'Social Science')

# 2.
def assert_student_completed_class(studentid, courseid):
    """Asserts that the specified student has completed the specified course."""
    +completed(studentid, courseid)

# 3.
def load_graduation_rules():
    """Loads rules for determining if a student has graduated."""
    # A student graduates if they have completed at least one course in each subject category.
    pyDatalog.load("""
        graduated(Student) <= completed(Student, Course) & subject(Course, Subject)
    """)

# 4.
def ask_if_graduated(studentid):
    """Determines if the given student has graduated or not."""
    return bool(pyDatalog.ask("graduated("+studentid+")"))

# 5.
def find_graduates():
    """Finds all graduates based on the defined rules."""
    res = set()
    ans = pyDatalog.ask("graduated(X)")
    if ans:
        for t in ans.answers:
            res.add(t[0])
    return res

def main():
    # Asserting course completions for students
    assert_student_completed_class('s001', 'psy150')
    assert_student_completed_class('s001', 'eng101')
    assert_student_completed_class('s001', 'mat167')
    assert_student_completed_class('s001', 'cs101')
    assert_student_completed_class('s002', 'psy150')
    assert_student_completed_class('s002', 'his110')  # Changed 'his101' to 'his110'
    assert_student_completed_class('s002', 'cs101')
    assert_student_completed_class('s002', 'mat167')

    # Load course catalog and graduation rules
    load_course_catalog()
    load_graduation_rules()

    # Check if each student has graduated
    print('Student s001 did ' +
          ('' if ask_if_graduated('s001') else 'not ') +
          'graduate.')
    
    print('Student s002 did ' +
          ('' if ask_if_graduated('s002') else 'not ') +
          'graduate.')

    # Adding additional students
    assert_student_completed_class('s003', 'eng101')
    assert_student_completed_class('s003', 'art310')
    assert_student_completed_class('s003', 'psy150')

    assert_student_completed_class('s004', 'mat167')
    assert_student_completed_class('s004', 'his110')
    
    print('Graduating students:', find_graduates())

if __name__ == '__main__':
    main()

Output:
    
Student s001 did graduate.
Student s002 did graduate.
Student s003 did not graduate.
Student s004 did graduate.
Graduating students: {'s001', 's002', 's004'}

