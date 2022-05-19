from django.urls import path

from . views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
]

#it's not recommended that you create all your routes in the project, you have to create a routes file (urls.py)
#inside your application, i.e here we did a .py (a python file) for urls from our aplication "core"