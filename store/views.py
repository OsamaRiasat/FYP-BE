from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RawMaterials, RMDemand, DemandedMaterials
from .serializers import RawMaterialSerializerRMCodeNumber, RawMaterialSerializerMaterialName, \
    RawMaterialSerializerInput, DemandedMaterialsSerializerInput, DemandedMaterialsDNoSerializer
from .serializers import RMDemandSerializerInput, RMDemandSerializerDNo

# GET APIS

class RMCodeView(APIView):
    serializer_class = RawMaterialSerializerRMCodeNumber

    def get(self, request, RMCode):
        checkInDB = RawMaterials.objects.filter(RMCode=RMCode)
        if checkInDB:
            dataAgainstRMCode = RawMaterials.objects.filter(RMCode=RMCode).values("Material", "Units", "Types")
            return Response(dataAgainstRMCode)
        else:
            return Response("Wrong Rmcode Number")

class MaterialNameView(APIView):
    serializer_class = RawMaterialSerializerMaterialName

    def get(self, request, Material):
        checkInDB = RawMaterials.objects.filter(Material=Material)
        if checkInDB:
            dataAgainstMaterialName = RawMaterials.objects.filter(Material=Material).values("Material", "Units", "Types")
            return Response(dataAgainstMaterialName)
        else:
            return Response("Wrong Material Name")

class RMDemandView(APIView):
    serializer_class = RMDemandSerializerDNo

    def get(self, request, DNo):
        checkInDB = RMDemand.objects.filter(DNo=DNo)
        if checkInDB:
            dataAgainstDNo = RMDemand.objects.filter(DNo=DNo).values("Date", "PlanNo", "CancelledDates", "PONo")
            return Response(dataAgainstDNo)
        else:
            return Response("Wrong DNo ")


class DemandedMaterialDNoView(APIView):
    serializer_class = DemandedMaterialsDNoSerializer

    def get(self, request, DNo):
        checkInDB = DemandedMaterials.objects.filter(DNo=DNo)
        if checkInDB:
            dataAgainstDNoinDemandMaterial = DemandedMaterials.objects.filter(DNo=DNo).values("DemandedQuantity",
                                                                                              "CurrentStock", "status",
                                                                                              "Priority", "RMCode")
            return Response(dataAgainstDNoinDemandMaterial)
        else:
            return Response("Wrong DNo ")

# INPUT APIS
# --------------------------------------------

class RawMaterialInputAPI(APIView):
    serializer_class = RawMaterialSerializerInput

    def post(self, request):
        dataa = {
            "RmCode": request.data['RMCode'],
            "Material": request.data['Material'],
            "Types": request.data['Types'],
        }
        serializer = RawMaterialSerializerInput(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(dataa)

        else:
            return Response("Serializer not valid")

        return Response("Check")

class RMDemandInputAPI(APIView):
    serializer_class = RMDemandSerializerInput

    def post(self, request):
        serializer = RMDemandSerializerInput(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)


class DemandedMaterialInputAPI(APIView):
    serializer_class = DemandedMaterialsSerializerInput

    def post(self, request):
        data = {
            "DemandedQuantity": request.data['DemandedQuantity'],
            "CurrentStock": request.data['CurrentStock'],
            "status": request.data['status'],
            "Priority": request.data['Priority'],
            "DNo": request.data['DNo'],
            "RMCode": request.data['RMCode']
        }
        serializer = DemandedMaterialsSerializerInput(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data)

        else:
            return Response("Serializer not valid")

        return Response("Check")

