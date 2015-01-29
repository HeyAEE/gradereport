#!/usr/bin/python

''' Parse_method.py - Converts a csv into a dict. '''

from emailgen.models import Topic, Student

def parse(fname):
    try:
        with open(fname, 'r') as f:
           keys = next(f).split(',')
           data = [row.split(',') for row in f]
           columns = map(list,zip(*data))
           grades = dict(zip(keys, columns))
           return grades
    except:
        print "Check filename and try again."
        
def to_student_array():
    grades = parse('precomp_practice.csv')
    height = len(grades.values()[1]) # Gets number of students.
    keys = grades.keys()
    a = []
    for x in xrange(0, height):
        name = grades[keys[0]][x].split()
        s, t_or_f = Student.objects.get_or_create(first_name=name[0], last_name=name[1])
        if t_or_f is False: # If it was already an entry
            s.recently_created=True # It's no longer a new one.
        else:
            a.append(s)
            s.recently_created=False # It's now a recently inserted student and should be referred to as such
        s.save()
        t = []
        for key in keys[1:]:
            topic, t_or_f_topic = Topic.objects.get_or_create(name=key, score=grades[key][x])
            if t_or_f_topic is True:
                a.append((name, topic))
            topic.save()
            t.append(topic)
        for unit in t:
            s.performance.add(unit)
    return a
