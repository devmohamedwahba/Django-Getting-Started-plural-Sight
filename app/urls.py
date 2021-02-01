from django.urls import path
from .views import index, details, new_meeting

urlpatterns = [
    path('home/', index, name='home'),
    path('details/<int:_id>', details, name='details'),
    path('new/', new_meeting, name='new'),
]
