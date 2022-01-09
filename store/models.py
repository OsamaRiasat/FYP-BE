from django.db import models


# Create your models here.


# A primitive extension of the standard User table from Django lib
class RawMaterials(models.Model):             #2 Api's
    ChoiceRole = (
        ("Leather", "Leather"),
        ("Paint", "Paint"),
        ("Iron", "Iron"),
        ("Plastic", "Plastic"),
    )
    RMCode = models.CharField(unique=True,max_length=20,null=False,help_text="RM01")
    Material = models.CharField(unique=True,max_length=20,null=False)
    Units = models.CharField(max_length=20, null=False)
    Types = models.CharField(default='Accounts', max_length=50, choices=ChoiceRole)

    def __str__(self):
        return str(self.RMCode)
        #return str('%s %s' % (self.RMCode, self.Material))


class RMDemand(models.Model):
    DNo = models.IntegerField(unique=True,  null=False, help_text="01")
    Date = models.DateField(null=False)    #2 Api   get Api , Dno given and whole data is return from table
    PlanNo = models.CharField(unique=True, max_length=20, null=False, help_text="PLN01")
    CancelledDates = models.DateField(null=False)
    PONo = models.CharField(unique=True, max_length=20, null=False, help_text="PON01")

    def __str__(self):
       # return self.PONo
       return str('%s %s' % (self.DNo, self.PONo))


class DemandedMaterials(models.Model):   # 1 Api to input data
    ChoiceRole = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    )
    DemandedQuantity = models.CharField(max_length=200, null=False)
    CurrentStock = models.CharField(max_length=200, null=False)
    status = models.CharField(max_length=200,null=False)
    Priority = models.CharField(default='1',max_length=50,choices=ChoiceRole)
    DNo = models.IntegerField(null=False)
    RMCode = models.ForeignKey(RawMaterials, to_field = 'RMCode', on_delete=models.CASCADE)

    def __str__(self):
        return str('%s %s %s' % (self.DemandedQuantity, self.DNo, self.Priority))

#--------------------------------------------------------------
class RMPurchaseOrder(models.Model):
    PONo = models.ForeignKey(RMDemand, to_field='PONo', on_delete=models.CASCADE,related_name='POOrder')
    OrderedDate=models.DateField(null=False)
    DNo = models.ForeignKey(RMDemand, to_field='DNo', on_delete=models.CASCADE,related_name='DNOOrder')

    def __str__(self):   #isma return koi unique karani ha?
        return str(self.PONo)

class Supplier(models.Model):
    SID=models.IntegerField(unique=True,null=False)
    Name=models.CharField(max_length=100,null=False)
    Email = models.CharField(max_length=100, null=False)
    City = models.CharField(max_length=100, null=False)
    Country = models.CharField(max_length=100, null=False)
    Phone = models.CharField(max_length=100, null=False)
    Material_Type=models.CharField(max_length=100,null=False)
    ContactPersonName=models.CharField(max_length=100,null=False)
    ContactPersonPhone=models.CharField(max_length=100,null=False)

    def __str__(self):
        return str(self.Email)
    #     return self.Email it return email when we use any column by foreign key in another table

class RMPurchaseOrderItem(models.Model):
    PONo = models.ForeignKey(RMDemand, to_field='PONo', on_delete=models.CASCADE)
    RMCode = models.ForeignKey(RawMaterials, to_field = 'RMCode', on_delete=models.CASCADE)
    Quantity=models.CharField(max_length=200,null=False)
    TotalAmount=models.CharField(max_length=200,null=False)
    Status=models.CharField(max_length=200,null=False)
    CommitedDates= models.DateField(null=False)
    Pending = models.CharField(max_length=200, null=False)
    Received = models.CharField(max_length=200, null=False)
    SID=models.ForeignKey(Supplier,to_field='SID',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.SID)    #Return Email from SID i.e unique