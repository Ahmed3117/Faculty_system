from django.urls import path
from .views import Login, ProfileEdit, profile, profile_list, subjects,last_profile,LastProfileEdit
from django.contrib.auth.views import LogoutView 

app_name = 'accounts'

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='about:list'), name="logout"),
    path('profile/',profile,name='profile'),
    path("subjects/", subjects, name="subjects"),
    path("profile-settings", profile_list, name="profile-settings"),
    path('profile-edit/<int:pk>',ProfileEdit.as_view(),name='profile-edit'),
    path("last-profile", last_profile, name="last-profile"),
    path('last-profile-edit/<int:pk>',LastProfileEdit.as_view(),name='last-profile-edit'),
]