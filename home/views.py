from django import apps
from django.shortcuts import render,HttpResponse

from home.models import Task

# nmot used
def basic(request):
    return  HttpResponse('This is used to check working of view to show page to user.')

#____________________________________________________________________


def home(request):
   context = {'success': False}
   if request.method == "POST":

     title = request.POST['title']
     desc = request.POST['desc']
     print(title, desc)

            # bind to model
     ins = Task(taskTitle=title, taskDesc=desc)
     ins.save()
     # It is used to show the alert of form submission to user
     context = {'success': True}

                     # If requuest is GET , then just show the Add Task Form
   return  render( request ,'home.html' , context)
        


#____________________________________________________________________


def taskList(request):
    allTasks= Task.objects.all()    
       #for item in allTasks:
           #print(item.taskTitle)
    context={'tasks':allTasks}
    
    return render(request , 'taskList.html' ,context)








#____________________________________________________________________
