from django.contrib import admin
from .models import RMDemand, RawMaterials, DemandedMaterials, RMPurchaseOrder, Supplier, RMPurchaseOrderItem

# Register your models here.

admin.site.register(RMDemand)
admin.site.register(RawMaterials)
admin.site.register(DemandedMaterials)
admin.site.register(RMPurchaseOrder)
admin.site.register(Supplier)
admin.site.register(RMPurchaseOrderItem)
