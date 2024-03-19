from .models import Product, profile,categories,orderDetail,orders,User
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['isStaff'] = user.is_staff
        token['isSuper'] = user.is_superuser

        
      
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = '__all__'
class ODetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderDetail
        fields = '__all__'
class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = '__all__'
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = '__all__'


@api_view(['GET'])
def index(req):
    return Response('hiiiiiii')


@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user born")

@api_view(['GET'])
def getImages(request):
    res=[] #create an empty list
    for img in Product.objects.all(): #run on every row in the table...
        res.append({"desc":img.desc,
                "price":img.price,
                "cat":img.cat,
               "image":str( img.image)
                }) #append row by to row to res list
    return Response(res) #return array as json response


# upload image method (with serialize)
class APIViews(APIView):
    parser_class=(MultiPartParser,FormParser)
    def post(self,request,*args,**kwargs):
        api_serializer=ProductSerializer(data=request.data)
       
        if api_serializer.is_valid():
            api_serializer.save()
            return Response(api_serializer.data,status=status.HTTP_201_CREATED)
        else:
            print('error',api_serializer.errors)
            return Response(api_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
class Products(APIView):
    def get(self, request):
        my_model = Product.objects.all()
        serializer = ProductSerializer(my_model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # usr =request.user
        # print(usr)
        serializer = ProductSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, id):
      try:
        product = Product.objects.get(id=id)
      except ObjectDoesNotExist:
        return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
      serializer = ProductSerializer(product, data=request.data)
      if serializer.is_valid():
        serializer.save()

        # Update the associated image if provided in the request
        if 'image' in request.data:
            product.image.delete()  # Delete the old image
            product.image = request.data['image']  # Assign the new image
            product.save()

        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


   
    def delete(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        # Delete the associated image if it exists
        if product.image:
            product.image.delete()

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    



class Cart(APIView):
    def get(self, request):
        my_model = Product.objects.all()
        serializer = ProductSerializer(my_model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # usr =request.user
        # print(usr)
        serializer = ProductSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, id):
      try:
        product = Product.objects.get(id=id)
      except ObjectDoesNotExist:
        return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
      serializer = ProductSerializer(product, data=request.data)
      if serializer.is_valid():
        serializer.save()

        # Update the associated image if provided in the request
        if 'image' in request.data:
            product.image.delete()  # Delete the old image
            product.image = request.data['image']  # Assign the new image
            product.save()

        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


   
    def delete(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        # Delete the associated image if it exists
        if product.image:
            product.image.delete()

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    