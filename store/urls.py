from django.urls import path, include
from .views import *

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'store'
urlpatterns = [
    path('RMCodeView/<str:RMCode>/', RMCodeView.as_view(), name='RMCode'),
    path('MaterialNameView/<str:Material>/', MaterialNameView.as_view(), name='MaterialName'),
    path('RawMaterialInput/', RawMaterialInputAPI.as_view(), name='RawMaterialInput'),
    path('RMDemandView/<str:DNo>/', RMDemandView.as_view(), name='RMDemandView'),
    path('RMDemandInput/', RMDemandInputAPI.as_view(), name='RMDemandInput'),
    path('DemandedMaterialView/<str:DNo>/', DemandedMaterialDNoView.as_view(), name='DemandedMaterial'),
]



