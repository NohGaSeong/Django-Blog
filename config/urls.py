from Blog import views
from django.urls import path
from django.contrib import admin

app_name = 'blog'
urlpatterns = [
   path('',views.hello, name = 'hello'),
   path('admin/', admin.site.urls),
   path('login/', views.login, name = 'login'),
   path('signup/', views.signup, name = 'signUp'),
   path('main/',views.main, name = 'main' ),
   ]
