from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from .models import User, Task

# Create your views here.
def index(request):
    if request.session.get('userId') == None:
        context = {
            'errors': request.session.get('errors'),
        }
    else:
        if Task.objects.filter(owner=request.session.get('userId')).count() > 0:
            context = {
                'errors': request.session.get('errors'),
                'currentUser': request.session.get('userName'),
                'tasks': Task.objects.get(owner=request.session.get('userId')),
            }
        else:
            context = {
                'errors': request.session.get('errors'),
                'currentUser': request.session.get('userName'),
                'tasks': None,
            }
    return render(request, 'todo/index.html', context)

def register(request):
    newName = request.POST['fl_name']
    newEmail = request.POST['email']
    newPassword = request.POST['password']
    newPasswordConfirm = request.POST['password_confirmation']
    if newPassword != newPasswordConfirm:
        request.session['errors']='Password does not match'
    elif User.objects.get(email=newEmail) == None:
        newUser = User(name=newName,email=newEmail,hashPassword=newPassword)
        newUser.save()
        request.session['userId']=newUser.id
        request.session['userName']=newUser.name
    else:
        request.session['errors']='Account with this email already exists!'
    return HttpResponseRedirect('todo/index.html')
    
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
    return HttpResponseRedirect('todo/index.html')
    
def logout(request):
    request.session.flush()
    return HttpResponseRedirect('todo/index.html')

def taskcreate(request):
    newTitle = request.POST['title']
    newOwner = request.session.get('userId')
    newDescription = request.POST['description']
    newCollaborator1 = request.POST['collaborator1']
    newCollaborator2 = request.POST['collaborator2']
    newCollaborator3 = request.POST['collaborator3']
    if newTitle != None:
        newTask = Task(title=newTitle,owner=newOwner,description=newDescription,collaborator1=newCollaborator1,collaborator2=newCollaborator2,collaborator3=newCollaborator3)
        request.session['errors']=None
    else:
        request.session['errors']='Error saving task.'
    return HttpResponseRedirect('todo/index.html')