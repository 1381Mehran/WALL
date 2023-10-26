from django.urls import path
from . import views


urlpatterns = [
    path('list/' , views.AdListView.as_view()),
    path('add/' , views.AdCreateView.as_view()),
    path('detail-edit/<int:pk>' , views.AdDetailEditView.as_view()),
]