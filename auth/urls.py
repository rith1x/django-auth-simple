from django.contrib import admin
from django.urls import path
from eyan import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.signIn, name="login"),
    path("postSignIn/", views.postSignIn, name="login-x"),
    path("signUp/", views.signUp, name="signup"),
    path("postSignUp/", views.postSignUp, name="signup-x"),
]
