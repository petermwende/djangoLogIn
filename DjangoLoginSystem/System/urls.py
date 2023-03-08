from django.contrib import admin
from django.urls import path,include
from djangoLoginSystem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="Home"),
    path('signup', views.signup, name="Signup"),
    path('signin', views.signin, name="Signin"),
    path('signout', views.signout, name="Signout"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
]