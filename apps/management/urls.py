from django.urls import path
from .views import *

app_name = 'management'


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('staff/', staff_list, name='staff'),
    path('staff/add/', AddStaff.as_view(), name='staff-add'),
    path('staff/<id>/', StaffDetails.as_view(), name='staff-details'),
    path('wards/', ManagerView.as_view(), name='wards'),
    path('ward/add/', AddWard.as_view(), name='ward-add'),
    path('ward/<id>/', ward_details, name='ward-details'),
]