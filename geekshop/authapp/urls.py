from django.urls import path

from authapp.views import LoginListView, RegisterListView, Logout, ProfileFormView

app_name = 'authapp'

urlpatterns = [
    path('login/', LoginListView.as_view(), name='login'),
    path('register/', RegisterListView.as_view(), name='register'),
    path('logaut/', Logout.as_view(), name='logaut'),
    path('profile/', ProfileFormView.as_view(), name='profile'),
]
