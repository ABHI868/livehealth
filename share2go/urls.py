

from django.urls import path
from .views import NoteCreateView,NoteRudAPIView,NoteListView
from share2go import views
urlpatterns=[

    path('add/',views.NoteCreateView.as_view(),name="create_notes"),
    path('list/',views.NoteListView.as_view(),name="list_notes"),
    path('list/<pk>/' ,views.NoteRudAPIView.as_view(),name="detail")
]