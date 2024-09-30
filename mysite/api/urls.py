from django.urls import path
from . import views

urlpatterns = [
    path("entry/", views.EntryListCreate.as_view(), name="entry-view-create"),
    path("entry/<int:pk>/", views.EntryRetrieveUpdateDestroy.as_view(), name="entry-view-retrieve-update-destroy")
]