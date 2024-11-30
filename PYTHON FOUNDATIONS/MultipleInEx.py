"""
1.Create multiple inheritance on
teacher,student and youtuber.

Q. if we have created teacher and now one
student joins master degree with becoming teacher
 then what??
Ans :  just make subclass from  teacher so that student will become teacher

2.Now student is teacher as well as youtuber then what???
-just use multiple inheritance for these three relations

"""

class Teacher:
    def teacher_action(self):
        print("I am a teacher")

class Science:
    def science_action(self):
        print("I am a scientist")

class Youtuber:
    def youtuber_action(self):
        print("I create content")

class Person(Teacher,Science,Youtuber):
    pass

c = Person()
c.teacher_action()
c.science_action()
c.youtuber_action()