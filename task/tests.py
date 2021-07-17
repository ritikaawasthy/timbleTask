from django.test import TestCase
from task.models import Student, Score, State
from task.forms import StudentForm, ScoreForm
from django.contrib.auth.models import User


# Create your tests here.
    
class Student_Form_Test(TestCase):
    def setup(self):
        stateObj=State.objects.create(name="Delhi")
        stateObj.save()

    # Valid Form Data
    def test_StudentForm_valid(self):
        stateObj=State.objects.create(name="Delhi")
        form = StudentForm(data={'name': "Trisha", 'rollNo': 555, 'state': [1]})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_StudentForm_invalid(self):
        form = StudentForm(data={'name': "", 'rollNo': 1 , 'state': [1]})
        self.assertFalse(form.is_valid())  

    def test_creation(self):
        stateObj= State.objects.create(name="Maharashtra")
        studentObj= Student.objects.create(name="Jennifer", rollNo=2)
        studentObj.state.add(1)
        studentObj.save()
        self.assertTrue(Student.objects.filter(rollNo=2).exists())

    def test_deletion(self):
        stateObj= State.objects.create(name="Gujrat")
        studentObj= Student.objects.create(name="Jhon", rollNo=3)
        studentObj.state.add(1)
        studentObj.save()
        getStuObj= Student.objects.filter(rollNo=3)
        getStuObj.delete()
        self.assertFalse(Student.objects.filter(rollNo=3).exists())

    def test_update(self):
        stateObj= State.objects.create(name="Uttar Pradesh")
        studentObj= Student.objects.create(name="jane", rollNo=4)
        studentObj.state.add(1)
        studentObj.save()
        getStuObj= Student.objects.filter(rollNo=4).update(name="jackson")
        stuObj=Student.objects.filter(rollNo=4).values('name')
        newName= stuObj[0]['name']
        self.assertTrue(newName=="jackson")







       

class Score_Form_Test(TestCase):

    # Valid Form Data
    def test_ScoreForm_valid(self):
        stateObj=State.objects.create(name="Delhi")
        studentObj=Student.objects.create(name="ritika", rollNo=1)
        studentObj.state.add(1)
        studentObj.save()
        form = ScoreForm(data={'subject': "django", 'marks': 80, 'student': 1})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_ScoreForm_invalid(self):
        form =  ScoreForm(data={'subject': "", 'marks': 80, 'student': 1})
        self.assertFalse(form.is_valid())   

    def test_creation(self):
        stateObj= State.objects.create(name="Sikkim")
        studentObj= Student.objects.create(name="Amy", rollNo=5555)
        studentObj.state.add(1)
        studentObj.save()
        scoreObj= Score.objects.create(subject="english", marks=90, student=studentObj)
        self.assertTrue(Score.objects.filter(marks=90).exists())
    
    def test_deletion(self):
        stateObj= State.objects.create(name="Gujrat")
        studentObj= Student.objects.create(name="Jhon", rollNo=3)
        studentObj.state.add(1)
        studentObj.save()
        getStuObj= Student.objects.filter(rollNo=3)
        scoreObj= Score.objects.create(subject="english", marks=90, student=studentObj)
        getScoreObj= Score.objects.filter(id=1)
        getScoreObj.delete()
        self.assertFalse(Score.objects.filter(id=1).exists())

    def test_update(self):
        stateObj= State.objects.create(name="Uttar Pradesh")
        studentObj= Student.objects.create(name="jane", rollNo=4)
        studentObj.state.add(1)
        studentObj.save()
        scoreObj= Score.objects.create(subject="english", marks=90, student=studentObj)
        getScoreObj= Score.objects.filter(student=1).update(marks=95)
        scoObj=Score.objects.filter(student=1).values('marks')
        newMarks= scoObj[0]['marks']
        self.assertTrue(newMarks==95)      

 
    