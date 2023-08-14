from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("market", views.market, name="market"),
    path("view_post/<str:pk>/", views.view_post, name="view_post"),

    
    path("register", views.register, name="register"),
    path("loginpage", views.loginView, name="loginView"),
    path("logoutpage", views.logoutView, name="logoutView"),


    path("publish", views.publish, name="publish"),
    path("profile", views.profile, name="profile"),
    path("edit/<str:pk>/", views.editpost, name="editpost"),
    path("delete/<str:pk>/", views.delete, name="deletepost"),
    path("update_profile", views.update_profile, name="update_profile"),

    path("reset_password", 
         auth_views.PasswordResetView.as_view(template_name="app/accounts/password_reset.html"), 
         name="password_reset"),

    path("password_reset_done", 
         auth_views.PasswordResetDoneView.as_view(template_name="app/accounts/password_reset_done.html"), 
         name="password_reset_done"),
    
    path("confirm/<uidb64>/<token>/", 
         auth_views.PasswordResetConfirmView.as_view(template_name="app/accounts/password_reset_confirm.html"), 
         name="password_reset_confirm"),
    
    path("reset_password_complete", 
         auth_views.PasswordResetCompleteView.as_view(template_name="app/accounts/password_reset_complete.html"), 
         name="password_reset_complete"),

     path("contactowner/<str:pk>/", views.contactowner, name="contactowner")


]