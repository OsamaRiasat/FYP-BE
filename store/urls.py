from django.urls import path, include
from .views import *

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'store'
urlpatterns = [
    # Two List views for RM Code and Name
    path('RMCodelist/', RMCodeslist.as_view(), name='RMCodeList'),
    path('Materiallist/', MaterialNameslist.as_view(), name='MaterialList'),
    # Two Get views for Raw material by RM Code and Name
    path('GetbyRMNo/<str:RMCode>/', GetRMbyCodeNo.as_view(), name='GetRawmaterialbyRMNo'),
    path('GetbyMaterial/<str:Material>/', GetRMbyName.as_view(), name='GetbyMaterialName'),
    # Post view for Raw materials
    path('InsertRawMaterial/', InsertRawMaterials.as_view(), name='InsertRawMaterial'),

    # Demand Table Views for GET & POST
    path('GetDemandbyDNo/<str:DNo>/', GetDemands.as_view(), name='GetDemand'),
    path('GetLatestDemand/', GetLatestDemanded.as_view(), name='GetLatestDemand'),
    path('InsertDemand/', InsertDemand.as_view(), name='InsertDemand'),

    # Demanded Items Table  Views for GET & POST
    path('GetDemandedMaterialsbyDNo/<str:DNo>/', GetDemandedMaterials.as_view(), name='GetDemandedMaterialsbyDNo'),


    #Urls of Supplier Table
    path('SupplierInput/',InsertSupplierData.as_view(),name='InputInSupplier'),
    path("SupplierByName/<str:Name>/",GetSupplierByName.as_view(),name='SupplierByName'),
    path("SupplierById/<str:SID>/",GetSupplierById.as_view(),name='SupplierById'),
    path("SupplierListByCity/<str:City>/",SupplierListByCity.as_view(),name='SupplierListByCity'),
    path("SupplierListByMaterialType/<str:Material_Type>/",SupplierListByMaterialType.as_view(),name='SupplierListByMaterialType'),


    #Urls of Purchase Order
    path('PurchaseOrderInput/',PurchaseOrderInput.as_view(),name='PurchaseOrderInput'),
    path("GetPurchaseOrderByPONo/<str:PONo>/",GetPurchaseOrderByPONo.as_view(),name='GetPurchaseOrderByPONo'),



    path('PurchaseOrderItemInput/',RMPurhcaseOrderItemInput.as_view(),name='RMPurhcaseOrderItemInput'),
    path("GetPurchaseItemsListByPONo/<str:PONo>/",GetPurchaseItemsListByPONoView.as_view(),name='GetPurchaseItemsListByPONo'),
    path("GetPurchaseItemsListBySID/<int:SID>/",GetPurchaseItemsListBySIDView.as_view(),name='GetPurchaseItemsListBySID'),
    path("GetPurchaseItemsListByStatus/<str:Status>/",GetPurchaseItemsListByStatusView.as_view(),name='GetPurchaseItemsListByStatus'),

    path("GetPurchaseItemByRMCode/<str:RMCode>/",GetPurchaseItemByRMCodeView.as_view(),name='GetPurchaseItemByRMCode'),
    #path("GetPurchaseItemsListByPONo/<str:PONo>/",GetPurchaseItemsListByPONo).as_view(),name='GetPurchaseItemsListByPONo')

]



