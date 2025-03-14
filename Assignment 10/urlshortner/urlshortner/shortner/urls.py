from django.urls import path
from .views import index, create, go

urlpatterns = [
    path("",view=index , name='index'),
    path("create",view=create , name='create'),
    path("<str:pk>", view=go, name="go"),
]