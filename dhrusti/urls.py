from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('patient_info', views.patient_info, name='patient_info'),
    # path('pdf', views.pdf, name='pdf'),
    path('patient_info_form', views.patient_info_form, name = 'patient_info_form'),
    # path('patient_detail<int:id>', views.patient_detail, name='patient_detail'),



]
