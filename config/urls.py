from django.contrib import admin
from Blog import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello, name = 'hello'),
    path('/login', views.login, name = 'login'),
]
