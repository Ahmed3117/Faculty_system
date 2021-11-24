from django.urls import path
from .api_view import FacultyList, FacultyCreate, FacultyRUD
from .views import faculty_information
app_name = 'about'

urlpatterns = [
    # api links
    path("api/facultyinfo/", FacultyList.as_view(), name="list"),
    path("api/facultycreate/", FacultyCreate.as_view(), name="create"),
    path("api/facultyrud/<int:pk>", FacultyRUD.as_view(), name="detail"),
    # static links
    path("", faculty_information, name="list"),
]