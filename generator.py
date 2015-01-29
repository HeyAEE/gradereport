#!/usr/bin/python

''' Generator.py - Generates grade report messages to students. '''

from emailgen.models import Student, Topic

test_dict = {'Unit 0':'Name','Units 1-3':'Cells - review', 'Units 4-5':'Classes of Macromolecules','Unit 6':'Transport Across Cell Membranes','Units 7-8':'Energy Use and Metabolism','Unit 9':'Mitosis'} # Should be changed on a per-test basis
    
def create_student_dict(student):
    # Used to create a dict for each student. Can be stored in array format.
    student_dict = {}
    student_dict['Name'] = student.first_name + " " + student.last_name
    student_dict['New'] = student.recently_created
    student_dict['Topics']= []
    for topic in student.performance.all():
        student_dict['Topics'].append(((topic.name).rstrip(),round(topic.score*100,1))) # key = topic name, value = score in percent
    return student_dict

def create_total_dict(student_dict):
    return

def email_render(student):
    return
