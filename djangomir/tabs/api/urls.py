from django.urls import path
from tabs.api.views import TabListAPIView, TabDetailView

urlpatterns = [
    path(r'', TabListAPIView.as_view(), name='list'),
    path('<int:id>/delete/', TabDetailView.as_view()),
    path('create/', TabDetailView.as_view()),
]