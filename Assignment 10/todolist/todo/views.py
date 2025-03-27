from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Todo




# Create your views here.
def index(request):
  todo =Todo.objects.all()
  if request.method == 'POST':
    new_todo = Todo(
      title = request.POST['title']
    )
    new_todo.save()
    return redirect('/')
    
  return render(request, 'index.html', {'todo':todo})

def delete(request , pk):
  todo = Todo.objects.get(id = pk)
  todo.delete()
  return redirect('/')
