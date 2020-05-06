from django.urls import path
from upload.api.views import *

urlpatterns = [
    path(r'list/', DocumentListAPIView.as_view(), name='list'),
    path('<int:id>/delete/', DocumentFileDetailView.as_view()),
    path('create/', DocumentFileDetailView.as_view()),
]