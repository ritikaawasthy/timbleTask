from django.shortcuts import render
from .forms import UserRegisterForm, StudentForm, ScoreForm, ExtendedUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Student, State, Score
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import QueryDict
from django.db.models import Avg
# Create your views here.

@login_required(login_url='loginView/')
def home(request):
    user= request.user
    print(user)
    scoreObj= Score.objects.all().values('subject')
    subjectObjList= list(scoreObj)
    subjectList=[]
    for sub in subjectObjList:
        subjectList.append(sub['subject'])

    if (request.method== "GET"):
        return render(request, 'home.html', {"user":user, "subjectList": subjectList})
    if (request.method=="POST"):
        data= request.POST
        subject= data['subject']
        state= data['state']
        score= Score.objects.filter(student__state= state, subject= subject).aggregate(Avg('marks'))
        avgMarks=score['marks__avg']
        msg="record added"
        return render(request, 'home.html', {"user":user,"msg": msg, "avgMarks": avgMarks})


@login_required(login_url='loginView/')
def addStudent(request):
    user= request.user
    if request.method=="GET" and user.is_staff==True :
        studentForm= StudentForm()
        scoreForm= ScoreForm()
        return render(request, 'addStudent.html', {"user":user,"studentForm":studentForm, "scoreForm": scoreForm})
    if request.method=="POST" and user.is_staff==True :
        msg="testing"
        data= request.POST
        print(data)
        dataScore=QueryDict('', mutable=True)
        studentForm= StudentForm(data)
        if (studentForm.is_valid()==True):
            studentForm.save()
            rollNo= data['rollNo']
            studentObj=Student.objects.filter(rollNo=rollNo).values('id')
            studentID=studentObj[0]['id']
            dataScore.update({"student": studentID, "subject": data['subject'] , "marks": data['marks']})
            scoreForm= ScoreForm(dataScore)
            if( scoreForm.is_valid() ==True):
                scoreForm.save()
                msg="added successfully"
            else:
                msg=scoreForm.errors
                print(msg)
        else:
            msg=studentForm.errors
            print(msg)
    else:
        msg="Only Admin allowed"
    return render(request, 'addStudent.html', {"user":user,"msg": msg})


def loginView(request):
    return render(request, 'login.html')

def Login(request):
    if request.method == 'POST':
        data= request.POST
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            return render(request,'home.html')
        else:
            data="Invalid Credentials"
            return render(request, 'login.html', {"data": data})

def signUpView(request):
    return render(request, 'signUp.html')

def signUp(request):
    if request.method=='POST':
        data= request.POST
        phoneNo= data['phoneNumber']
        userName= data['username']
        dataEx=QueryDict('', mutable=True)
        form = UserRegisterForm(data)
        print(form.is_valid())
        if (form.is_valid()==True):
            form.save()
            userObj=User.objects.filter(username=userName).values('id')
            print(userObj)
            user=userObj[0]['id']
            dataEx.update({'phoneNumber': phoneNo, 'user':user })
            print(dataEx)
            formEx= ExtendedUserForm(dataEx)
            print(formEx.is_valid())
            if(formEx.is_valid()==True):
                formEx.save()
                return render(request, 'home.html')
            else:
                data="could not save phone number"
                return render(request, 'signUp.html', {"data": data})
        else:
            data= form.errors
            print(form.errors)
            return render(request, 'signUp.html', {"data": data})

def logoutView(request):
    logout(request)
    return render(request,'home.html')
'''
@login_required
def addStudents(request):
    if (request.user.is_staff==True):
        return render(request, '.html', {"data": data})

    else:
        data="Only admin users allowed"
        return render(request, 'signUp.html', {"data": data})
'''
