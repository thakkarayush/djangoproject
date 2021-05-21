from django.urls import path
from . import views
urlpatterns=[
    path("new/",views.StudentEntryView.as_view(),name="student-new"),
    path("view/",views.StudentListView.as_view(),name="student-view"),
    path("update/<int:pk>",views.StudentUpdateView.as_view(),name="student-update"),
    path("detail/<int:pk>",views.StudentDetailView.as_view(),name="student-detail"),
    path("delete/<int:pk>",views.StudentDeleteView.as_view(),name="student-delete")
]