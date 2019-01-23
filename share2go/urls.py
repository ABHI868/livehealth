

from django.urls import path
from .views import NoteCreateView,NoteRudAPIView
from share2go import views
urlpatterns=[

    path('add/notes',views.NoteCreateView.as_view(),name="create_notes"),
    path('notes/<pk>/' ,views.NoteRudAPIView.as_view(),name="detail")
]