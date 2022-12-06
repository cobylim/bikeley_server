from django.urls import path, include
from locations import views

urlpatterns = [
    path('v1/locations/', views.LocationList.as_view()),
    path('v1/locations/<int:pk>', views.LocationDetail.as_view()),
]