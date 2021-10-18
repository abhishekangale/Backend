from django.urls import path

from . import views

urlpatterns = [
    path('mentor', views.MentorAPIView.as_view(), name='mentor'),
    path('upsolve/', views.UpsolveContestAPIView.as_view(), name="cf_upsolve"),
    path('testing', views.testing),
    path('rating-change-email', views.rating_change_email)
]
