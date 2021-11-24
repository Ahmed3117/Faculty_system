from django.urls import path
from .views import Login, profile, subjects
#logout doesn't need view function or class . just import LogoutView and make the url
from django.contrib.auth.views import LogoutView 

app_name = 'accounts'

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='about:list'), name="logout"),
    path('profile/',profile,name='profile'),
    path("subjects/", subjects, name="subjects"),
]