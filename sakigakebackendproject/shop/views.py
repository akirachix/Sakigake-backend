from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Shop
from .serializers import  ShopSerializer

class ShopView(APIView):
    def get(self,request):
        try:
            shop = Shop.objects.all()
            serializer = ShopSerializer(shop,many=True)
            return Response(serializer.data ,status=status.HTTP_200_OK)
        except Exception as e:
            return Response ({"error":"An error occurred while fetching shops"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    def post(self,request):
        try:
            serializer = ShopSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":"An error occurred when creating a new assignment"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    
class ShopDetailView(APIView):
    def get(self,request,id,format=None):
        try:
            shop = Shop.objects.get(id=id)
            serializer = ShopSerializer(shop)
            return Response(serializer.data)
        except Shop.DoesNotExist:
            return Response({"error":"Shop not found"},status=status.HTTP_404_NOT_FOUND)

    

    def put(self, request, id, format=None):
        try:
            shop = Shop.objects.get(id=id)
            serializer = ShopSerializer(shop, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Shop.DoesNotExist:
            return Response({"error": "Shop not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,id):
        try:
            shop = Shop.objects.get(id=id)
            shop.delete()
            return Response ({"message":"Shop deleted"}, status=status.HTTP_410_GONE)
        except Shop.DoesNotExist:
            return Response({"error":"Shop not found"},status=status.HTTP_404_NOT_FOUND)
        

    
        

    
        




