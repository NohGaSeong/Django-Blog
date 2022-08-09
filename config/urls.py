from Blog import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
   path('',views.hello, name = 'hello'),
   path('admin/', admin.site.urls),
   path('login/', views.login, name = 'login'),
   path('signup/', views.signup, name = 'signup'),
]
