from rest_framework import serializers

from .models import RawMaterials, RMDemand, DemandedMaterials, Supplier, RMPurchaseOrder, RMPurchaseOrderItem


# RAW Material Table Serializers
class RMCodeNumberSerializer(serializers.ModelSerializer):
    RMCode=serializers.CharField(max_length=100,required=True)
    class Meta:
        model=RawMaterials
        fields=['RMCode']

class MaterialNameSerializer(serializers.ModelSerializer):
    Material=serializers.CharField(max_length=100,required=True)
    class Meta:
        model=RawMaterials
        fields=['Material']


class RawMaterialInputSerializer(serializers.ModelSerializer):

    RMCode=serializers.CharField(max_length=100,required=True,write_only=True)
    Material = serializers.CharField(max_length=100, required=True, write_only=True)
    Units = serializers.CharField(max_length=100, required=True, write_only=True)
    Types = serializers.CharField(max_length=100, required=True,write_only=True)
    class Meta:
        model=RawMaterials
        fields=['RMCode','Material','Units','Types']

# DemandedMaterials Table Serializers
class DemandedMaterialsSerializer(serializers.ModelSerializer):
   class Meta:
        model=DemandedMaterials
        fields=['DNo']

# Input Serializer
class DemandedMaterialsInputSerializer(serializers.ModelSerializer):
    class Meta:
        model=DemandedMaterials
        fields='__all__'

# Demand Table Serilaizers
class DemandSerializer(serializers.ModelSerializer):
    DNo = serializers.CharField(max_length=20, help_text="DN01")
    class Meta:
        model=RMDemand
        fields=['DNo']

# Input Serializer
class DemandSerializerInput(serializers.ModelSerializer):
    DNo = serializers.CharField(max_length=20, help_text="DN01")
    Date = serializers.DateField(required=True)
    PlanNo = serializers.CharField(max_length=20)
    CancelledDates = serializers.DateField(required=True)
    PONo = serializers.CharField(max_length=20)
    material = DemandedMaterialsInputSerializer(many=True,write_only=True)
    class Meta:
        model = RMDemand
        fields = ['DNo','Date','PlanNo','CancelledDates','PONo','material']

    def create(self, validated_data):
        material_data = validated_data.pop('material')
        demand = RMDemand.objects.create(**validated_data)
        for materials_data in material_data:
            DemandedMaterials.objects.create(**materials_data)
        return demand


#Supplier Table Api's Input
class SupplierInputSerializer(serializers.ModelSerializer):
    SID = serializers.IntegerField(required=True)
    Name = serializers.CharField(max_length=100, required=True)
    Email = serializers.CharField(max_length=100, required=True)
    City = serializers.CharField(max_length=100, required=True)
    Country = serializers.CharField(max_length=100, required=True)
    Phone = serializers.CharField(max_length=100, required=True)
    Material_Type = serializers.CharField(max_length=100, required=True)
    ContactPersonName = serializers.CharField(max_length=100, required=True)
    ContactPersonPhone = serializers.CharField(max_length=100, required=True)

    class Meta:
        model=Supplier
        fields=['SID','Name','Email','City','Country','Phone','Material_Type','ContactPersonName','ContactPersonPhone']

class GetSupplierByNameSerializer(serializers.ModelSerializer):
    Name=serializers.CharField(max_length=100, required=True)
    class Meta:
        model=Supplier
        fields=['Name']

class GetSupplierByIdSerializer(serializers.ModelSerializer):
    SID=serializers.CharField(required=True)
    class Meta:
        model=Supplier
        fields=['SID']

class GetSupplierListByCitySerializer(serializers.ModelSerializer):
    City=serializers.CharField(required=True)
    class Meta:
        model=Supplier
        fields=['City']

class GetSupplierListByMaterialTypeSerializer(serializers.ModelSerializer):
    Material_Type=serializers.CharField(required=True)
    class Meta:
        model=Supplier
        fields=['Material_Type']

#-----------------------------------------------------------------------------------------

#Purchase Order Serializer's

class PurchaseOrderInputSerializer(serializers.ModelSerializer):
    # PONo = serializers.ForeignKey(required=True)
    OrderedDate = serializers.DateField(required=True)
    #DNo = serializers.ForeignKey(required=True)

    class Meta:
        model=RMPurchaseOrder
        fields=['PONo','OrderedDate','DNo']

class RMPurchaseOrderByPONoSerializer(serializers.ModelSerializer):
    #PONo = serializers.ForeignKey(required=True)

    class Meta:
        model=RMPurchaseOrder
        fields=['PONo']

#---------------------------------------------------------

#PurhcaseOrderItem  Api's Table
class RMPurhcaseOrderItemInputSerializer(serializers.ModelSerializer):
    #PONo = models.ForeignKey(RMDemand, to_field='PONo', on_delete=models.CASCADE)
    #RMCode = models.ForeignKey(RawMaterials, to_field='RMCode', on_delete=models.CASCADE)
    Quantity = serializers.CharField(required=True)
    TotalAmount = serializers.CharField(required=True)
    Status = serializers.CharField(required=True)
    CommitedDates = serializers.DateField(required=True)
    Pending = serializers.CharField(required=True)
    Received = serializers.CharField(required=True)
    #SID = models.ForeignKey(Supplier, to_field='SID', on_delete=models.CASCADE)

    class Meta:
        model=RMPurchaseOrderItem
        #fields=['PONo','RMCode','Quantity','TotalAmount','Status','CommitedDates','Pending','Received','SID']
        fields='__all__'

class PurchaseItemsListByPONoSerializer(serializers.ModelSerializer):
    class Meta:
        model=RMPurchaseOrderItem
        fields=['PONo']

class PurchaseItemsListBySIDSerializer(serializers.ModelSerializer):
    class Meta:
        model=RMPurchaseOrderItem
        fields=['SID']

class PurchaseItemsListByStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=RMPurchaseOrderItem
        fields=['Status']

class PurchaseItemByRMCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=RMPurchaseOrderItem
        fields=['RMCode']