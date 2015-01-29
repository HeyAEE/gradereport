from django import template

register = template.Library()

@register.filter(name='gradecomment')
def gradecomment(grade):
    # grade = 100*grade # Converts to percentage
    if grade < 60:
        return "Get help on this topic.  Come to student hours for help.  High priority study topic."
    elif grade >= 80:
        return "Shows mastery of this topic.  Your hard work has paid off.  Low priority study topic."
    else:
        return "Approaching mastery.  Keep up the hard work.  Medium priority study topic."
        
@register.filter(name='get_value')
def get(student, key):
    return student.get(key,'')
