from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create-team/',		views.create_team,		name='create_team'),
    path('join-team/',			views.join_team,		name='join_team'),
    path('dashboard/',			views.dashboard,		name='dashboard'),
    path('',                    views.home,             name='home'),
    path('leave-team',          views.leave_team,       name='leave-team'),
    path('update-position/',    views.assign_position,  name='update-position'),
    path('submit-ppt/<int:pk>', views.submit_ppt,		name='submit_ppt'),
]