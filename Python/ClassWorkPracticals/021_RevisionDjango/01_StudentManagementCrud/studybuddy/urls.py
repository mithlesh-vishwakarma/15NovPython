from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from studybuddy.views import *

urlpatterns = [
    path("",index,name="index"),
    path("create",create,name="create"),
    path("display_student",display_student,name="display_student"),
    path ("delete",delete,name="delete"),
    path("update",update,name="update")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)