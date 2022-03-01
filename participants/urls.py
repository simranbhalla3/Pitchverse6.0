from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('past-events/',views.gallery,name='gallery'),
   path('excel-preevent/',views.export_answers_xls,name='export_answers_xls'),
    path('pre-event-reg/',views.pre_event_reg,name='pre-event-reg'),
    
]