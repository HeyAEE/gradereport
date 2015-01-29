#!/usr/bin/env python

import generator
from emailgen.models import Student, Topic
from django.template.loader import get_template
from django.template import Template, Context

def generate(student):
    moh = generator.create_student_dict(student)
    t = get_template('emailtemplate.txt')
    c = Context(moh)
    message = t.render(c)
    first_name, last_name = moh["Name"].split(" ")
    letter = open(last_name + "_" + first_name +".txt", 'w')
    letter.write(message)
    letter.close()

def run():    
    students = Student.objects.filter(recently_created=False)
    for student in students:
        print student
        generate(student)
