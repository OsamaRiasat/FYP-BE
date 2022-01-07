from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RawMaterials, RMDemand, DemandedMaterials, Supplier, RMPurchaseOrder, RMPurchaseOrderItem
from .serializers import RMCodeNumberSerializer, MaterialNameSerializer, \
    RawMaterialInputSerializer, DemandedMaterialsSerializer, DemandedMaterialsInputSerializer, \
    DemandSerializer, DemandSerializerInput, SupplierInputSerializer, GetSupplierByNameSerializer, \
    GetSupplierByIdSerializer, GetSupplierListByCitySerializer, GetSupplierListByMaterialTypeSerializer, \
    PurchaseOrderInputSerializer, RMPurchaseOrderByPONoSerializer, RMPurhcaseOrderItemInputSerializer, \
    PurchaseItemsListByPONoSerializer, PurchaseItemsListBySIDSerializer, PurchaseItemsListByStatusSerializer, \
    PurchaseItemByRMCodeSerializer


# GET APIS FOR Raw Material Table
class RMCodeslist(APIView):
    serializer_class = RMCodeNumberSerializer

    def get(self, request):
        RMcodelist = RawMaterials.objects.all()
        serializer = RMCodeNumberSerializer(RMcodelist, many=True)
        return Response(serializer.data)

class MaterialNameslist(APIView):
    serializer_class = MaterialNameSerializer

    def get(self, request):
        materiallist = RawMaterials.objects.all()
        serializer = MaterialNameSerializer(materiallist, many=True)
        return Response(serializer.data)

class GetRMbyCodeNo(APIView):
    serializer_class = RMCodeNumberSerializer

    def get(self, request, RMCode):
        checkInDB = RawMaterials.objects.filter(RMCode=RMCode)
        if checkInDB:
            dataAgainstRMCode = RawMaterials.objects.filter(RMCode=RMCode).values("Material", "Units", "Types")
            return Response(dataAgainstRMCode)
        else:
            return Response("Wrong Rmcode Number")

class GetRMbyName(APIView):
    serializer_class = MaterialNameSerializer

    def get(self, request, Material):
        checkInDB = RawMaterials.objects.filter(Material=Material)
        if checkInDB:
            dataAgainstMaterialName = RawMaterials.objects.filter(Material=Material).values("Material", "Units", "Types")
            return Response(dataAgainstMaterialName)
        else:
            return Response("Wrong Material Name")

# Input APIS FOR Raw Material Table
class InsertRawMaterials(APIView):
    serializer_class = RawMaterialInputSerializer

    def post(self, request):
        dataa = {
            "RmCode": request.data['RMCode'],
            "Material": request.data['Material'],
            "Types": request.data['Types'],
        }
        serializer = RawMaterialInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(dataa)

        else:
            return Response("Serializer not valid")

        return Response("Check")

# GET APIS FOR Demand Table
class GetDemands(APIView):
    serializer_class = DemandSerializer

    def get(self, request, DNo):
        checkInDB = RMDemand.objects.filter(DNo=DNo)
        if checkInDB:
            dataAgainstDNo = RMDemand.objects.filter(DNo=DNo).values("Date", "PlanNo", "CancelledDates", "PONo")
            return Response(dataAgainstDNo)
        else:
            return Response("Wrong DNo ")

class GetLatestDemanded(APIView):
    serializer_class = DemandedMaterialsSerializer

    def get(self, request):
        latestDemand = RMDemand.objects.latest('DNo')
        return Response(latestDemand.DNo)

# Input APIS FOR Demand Table
class InsertDemand(APIView):
    serializer_class = DemandSerializerInput

    def post(self, request):
        serializer = DemandSerializerInput(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)

# GET APIS FOR Demanded Item Table
class GetDemandedMaterials(APIView):
    serializer_class = DemandedMaterialsSerializer

    def get(self, request, DNo):
        checkInDB = DemandedMaterials.objects.filter(DNo=DNo)
        if checkInDB:
            dataAgainstDNoinDemandMaterial = DemandedMaterials.objects.filter(DNo=DNo).values("DemandedQuantity",
                                                                                              "CurrentStock", "status",
                                                                                              "Priority", "RMCode")
            return Response(dataAgainstDNoinDemandMaterial)
        else:
            return Response("Wrong DNo ")

# Input APIS FOR Demanded Item Table
class InsertDemandedMaterials(APIView):
    serializer_class = DemandedMaterialsInputSerializer

    def post(self, request):
        data = {
            "DemandedQuantity": request.data['DemandedQuantity'],
            "CurrentStock": request.data['CurrentStock'],
            "status": request.data['status'],
            "Priority": request.data['Priority'],
            "DNo": request.data['DNo'],
            "RMCode": request.data['RMCode']
        }
        serializer = DemandedMaterialsInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data)

        else:
            return Response("Serializer not valid")

        return Response("Check")

#----------------------------------------------------------------------------------------
#Supplier Order Table API's

class InsertSupplierData(APIView):
    serializer_class=SupplierInputSerializer

    def post(self,request):
        data = {
            "SID": request.data['SID'],
            "Name":request.data['Name'],
            "Email":request.data['Email'],
            "City":request.data['City'],
            "Country":request.data['Country'],
            "Phone":request.data['Phone'],
            "Material_Type":request.data['Material_Type'],
            "ContactPersonName":request.data['ContactPersonName'],
            "ContactPersonPhone":request.data['ContactPersonPhone']
        }
        serializer = SupplierInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data)

        else:
            return Response("Serializer not valid")

        return Response("Check")

class GetSupplierByName(APIView):
    serializer_class=GetSupplierByNameSerializer

    def get(self,request,Name):
        checkNameInDB=Supplier.objects.filter(Name=Name)

        if checkNameInDB:
            getDataFromSupplier=Supplier.objects.filter(Name=Name).values("SID","Email","City","Country","Phone",
                                                                          "Material_Type","ContactPersonName",
                                                                          "ContactPersonPhone")
            return Response(getDataFromSupplier)
        else:
            return Response("Wrong Name")

class GetSupplierById(APIView):
    serializer_class = GetSupplierByIdSerializer

    def get(self, request, SID):
        checkIdInDB = Supplier.objects.filter(SID=SID)
        if checkIdInDB:
            getDataFromSupplier = Supplier.objects.filter(SID=SID).values("Name", "Email", "City", "Country", "Phone",
                                                                            "Material_Type", "ContactPersonName",
                                                                            "ContactPersonPhone")
            return Response(getDataFromSupplier)
        else:
            return Response("Wrong ID")

class SupplierListByCity(APIView):
    serializer_class=GetSupplierListByCitySerializer

    def get(self,request,City):
        checkIdInDB = Supplier.objects.filter(City=City)
        if checkIdInDB:
            getData=Supplier.objects.filter(City=City).values("Name","Email","Phone")
            getDataList=list(getData)

            return Response(getDataList)
        else:
            return Response("Wrong City")

class SupplierListByMaterialType(APIView):
    serializer_class=GetSupplierListByMaterialTypeSerializer

    def get(self,request,Material_Type):
        checkIdInDB = Supplier.objects.filter(Material_Type=Material_Type)
        if checkIdInDB:
            getData=Supplier.objects.filter(Material_Type=Material_Type).values("Name","Email","Phone")
            getDataList=list(getData)

            return Response(getDataList)
        else:
            return Response("Wrong Material_Type")

#----------------------------------------------------------------------------------------

#Api's of Purchase Order Table

class PurchaseOrderInput(APIView):
    serializer_class=PurchaseOrderInputSerializer

    def post(self,request):
        data:{
            "PONo":request.data['PONo'],
            "OrderedDate":request.data['OrderedDate'],
            "DNo":request.data['DNo']
        }

        serializer=PurchaseOrderInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Serializer not valid")

        return Response("Check")

class GetPurchaseOrderByPONo(APIView):            #Issue in this API , PoNo is in format, not individually return
    serializer_class=RMPurchaseOrderByPONoSerializer

    def get(self,request,PONo):
        checkIdInDB = RMPurchaseOrder.objects.filter(PONo=PONo)
        if checkIdInDB:
            getData = RMPurchaseOrder.objects.filter(PONo=PONo).values("OrderedDate","DNo")
            getDataList = list(getData)

            return Response(getDataList)
        else:
            return Response("Wrong PONo")

#---------------------------------------------------------------------------------

#  Api's of purhcase order item Table
class RMPurhcaseOrderItemInput(APIView):
    serializer_class=RMPurhcaseOrderItemInputSerializer

    def post(self,request):
        data={
            "PONo":request.data['PONo'],
            "RMCode":request.data['RMCode'],
            "Quantity":request.data['Quantity'],
            "TotalAmount":request.data['TotalAmount'],
            "Status":request.data['Status'],
            "CommitedDates":request.data['CommitedDates'],
            "Pending":request.data['Pending'],
            "Received":request.data['Received'],
            "SID":request.data['SID']
        }

        serializer=RMPurhcaseOrderItemInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Serializer not valid")

        return Response("Check")

class GetPurchaseItemsListByPONoView(APIView):
    serializer_class=PurchaseItemsListByPONoSerializer

    def get(self,request,PONo):
        checkInDB = RMPurchaseOrderItem.objects.filter(PONo=PONo)
        if checkInDB:
            getData = RMPurchaseOrderItem.objects.filter(PONo=PONo).values("SID","RMCode", "Quantity","TotalAmount",
                                                                           "Status","CommitedDates","Received","Pending")
            getDataList = list(getData)

            return Response(getDataList)
        else:
            return Response("Wrong PONo")

class GetPurchaseItemsListBySIDView(APIView):
    serializer_class=PurchaseItemsListBySIDSerializer

    def get(self,request,SID):
        checkInDB = RMPurchaseOrderItem.objects.filter(SID=SID)
        if checkInDB:
            getData = RMPurchaseOrderItem.objects.filter(SID=SID).values("PONo","RMCode", "Quantity","TotalAmount",
                                                                           "Status","CommitedDates","Received","Pending")
            getDataList = list(getData)

            return Response(getDataList)
        else:
            return Response("Wrong SID")


class GetPurchaseItemsListByStatusView(APIView):
    serializer_class=PurchaseItemsListByStatusSerializer

    def get(self,request,Status):
        checkInDB = RMPurchaseOrderItem.objects.filter(Status=Status)
        if checkInDB:
            getData = RMPurchaseOrderItem.objects.filter(Status=Status).values("PONo","RMCode", "Quantity","TotalAmount","SID"
                                                                           ,"CommitedDates","Received","Pending")
            getDataList = list(getData)

            return Response(getDataList)
        else:
            return Response("Wrong Status")

class GetPurchaseItemByRMCodeView(APIView):
    serializer_class=PurchaseItemByRMCodeSerializer

    def get(self,request,RMCode):
        checkInDB = RMPurchaseOrderItem.objects.filter(RMCode=RMCode)
        if checkInDB:
            getData = RMPurchaseOrderItem.objects.filter(RMCode=RMCode).values("PONo","Status", "Quantity","TotalAmount","SID"
                                                                           ,"CommitedDates","Received","Pending")
            getDataList = list(getData)

            return Response(getDataList)
        else:
            return Response("Wrong RMCode")