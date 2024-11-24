from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from api.models import Vehicle

from api.serializers import VehicleSerializer,SignUpSerializer

from rest_framework import authentication,permissions

# Create your views here.

class VehicleListCreateView(APIView):

    serializer_class=VehicleSerializer

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):

        qs=Vehicle.objects.all()

        if "fuel_item" in request.query_params:

            filter_text=request.query_params.get("fuel_type")

            qs=qs.filter(fuel_type=filter_text)

        serializer_instance=self.serializer_class(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request,*args,**kwargs):

        serializer_instance=self.serializer_class(data=request.data) 

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data) 

        return Response(data=serializer_instance.errors)    


class VehcileRetrieveUpdateDestroyView(APIView):

    serializer_class=VehicleSerializer

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Vehicle.objects.get(id=id)

        serializer_instance=self.serializer_class(qs)

        return Response(data=serializer_instance.data)


    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        vehicle_object=Vehicle.objects.get(id=id)  

        serializer_instance=self.serializer_class(data=request.data,instance=vehicle_object)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)    

        return Response(data=serializer_instance.errors) 


    def delete(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Vehicle.objects.get(id=id).delete()

        return Response(data={"message":"deleted"})


class VehicleFuelTypeView(APIView):

    serializer_class=VehicleSerializer

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]
    
    def get(self,request,*args,**kwargs):

        fuel_types=[ft[0] for ft in Vehicle.fuel_type]

        return Response(data=fuel_types)

  

class SignUpView(APIView):

    serializer_class=SignUpSerializer

    def post(self,request,*args,**kwargs):

        serializer_instance=self.serializer_class(data=request.data)  

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        return Response(data=serializer_instance.data)    