from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.db.models import Q

from .models import User, Task

# Create your views here.
def index(request):
    if request.session.get('userId') == None:
        context = {
            'errors': request.session.get('errors'),
            'currentUser': None,
        }
    else:
        currentUser=User.objects.get(id=request.session.get('userId'))
        if Task.objects.filter(Q(owner=currentUser.id) | Q(collaborator1=currentUser.email) | Q(collaborator2=currentUser.email) | Q(collaborator3=currentUser.email)).count() > 0:
            context = {
                'errors': request.session.get('errors'),
                'currentUser': currentUser,
                'tasks': Task.objects.filter(Q(owner=currentUser.id) | Q(collaborator1=currentUser.email) | Q(collaborator2=currentUser.email) | Q(collaborator3=currentUser.email)),
            }
        else:
            context = {
                'errors': request.session.get('errors'),
                'currentUser': currentUser,
                'tasks': None,
            }
    return render(request, 'todo/index.html', context)

def register(request):
    newName = request.POST['fl_name']
    newEmail = request.POST['email']
    newPassword = request.POST['password']
    newPasswordConfirm = request.POST['password_confirmation']
    if len(newName) < 1 or len(newName) > 50:
        request.session['errors']='Invalid Name Length'
    elif len(newEmail) < 1 or len(newEmail) > 50:
        request.session['errors']='Invalid Email Length'
    elif len(newPassword) < 1 or len(newPassword) > 50:
        request.session['errors']='Invalid Password Length'
    else:
        if newPassword != newPasswordConfirm:
            request.session['errors']='Password does not match'
        elif User.objects.filter(email=newEmail).count() == 0:
            newUser = User(name=newName,email=newEmail,hashPassword=newPassword)
            newUser.save()
            request.session['userId']=newUser.id
            request.session['userName']=newUser.name
        else:
            request.session['errors']='Account with this email already exists!'
    return HttpResponseRedirect('/')
    
def login(request):
    checkEmail = request.POST['email']
    checkPassword = request.POST['password']
    if User.objects.filter(email=checkEmail).count() > 0:
        currentUser = User.objects.get(email=checkEmail)
        if currentUser.hashPassword!=checkPassword:
            request.session['errors'] = 'Invalid password.'
        else:    
            request.session['userId']=currentUser.id
            request.session['userName']=currentUser.name
    else:
        request.session['errors'] = 'Invalid email address'
    return HttpResponseRedirect('/')
    
def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')

def taskcreate(request):
    newTitle = request.POST['title']
    newOwner = request.session.get('userId')
    newDescription = request.POST['description']
    newCollaborator1 = request.POST['collaborator1']
    newCollaborator2 = request.POST['collaborator2']
    newCollaborator3 = request.POST['collaborator3']
    if newTitle != None:
        newTask = Task(title=newTitle,owner=newOwner,description=newDescription,collaborator1=newCollaborator1,collaborator2=newCollaborator2,collaborator3=newCollaborator3,isComplete=False)
        newTask.save()
        request.session['errors']=None
    else:
        request.session['errors']='Error saving task.'
    return HttpResponseRedirect('/')

def taskdelete(request):
    deleteId = request.POST['deleteId']
    Task.objects.get(id=deleteId).delete()
    return HttpResponseRedirect('/')

def tasktoggle(request):
    toggleId = request.POST['taskId']
    newStatus = request.POST['changeStatus']
    if newStatus == "1":
        Task.objects.filter(id=toggleId).update(isComplete=True)
    else:
        Task.objects.filter(id=toggleId).update(isComplete=False)
    return HttpResponseRedirect('/')