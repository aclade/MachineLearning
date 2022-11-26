class ClassSchedule:
   def __init__(self, course):
       self.course = course
 
   def __del__(self):
       print('You successfully deleted your schedule')

# create a ClassSchedule object
sched = ClassSchedule('Chemistry')
# delete the ClassSchedule object
print(sched.course)
