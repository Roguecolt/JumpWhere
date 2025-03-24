from django.shortcuts import render , HttpResponse, redirect
import uuid
from .models import url

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == "POST":
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = url(link=link, uuid=uid)
        new_url.save()
        return render(request,'index.html',{"uid":uid})
    

def go(request, pk):
    url_details = url.objects.get(uuid=pk)
    return redirect(url_details.link)