from django.shortcuts import render
from django.http import HttpResponse


from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .serialiser import RegisterSerializer, ProductSerializer
from django.http.response import JsonResponse
@api_view(['POST'])
# Create your views here.
def create_account(request):
    print("Entering to create account method")
    # return HttpResponse("creating an account")
    python_obj = JSONParser().parse(request)
    print(python_obj)

    # to map python obj to table in db

    serialized_obj = RegisterSerializer(data=python_obj)
    print(serialized_obj)
    if serialized_obj.is_valid():
        print("Data is valid")
        serialized_obj.save()
        return JsonResponse(serialized_obj.data)
    else:
        print("Data is invalid")
        return JsonResponse(serialized_obj.errors)

from .models import Register
@api_view(['GET'])
def getUsers(request):
    print("Enterining get user method")
    registerFromDb = Register.objects.all()
    print(registerFromDb)
    serialize_obj = RegisterSerializer(registerFromDb, many=True)
    print(serialize_obj)
    return JsonResponse(serialize_obj.data, safe=False)

@api_view(['PUT'])
def updatebyId(request, pk):
    print("Entering to upadatebyId")
    register_fromtable = Register.objects.get(pk=pk)
    print(register_fromtable)
    requestFromUser = JSONParser().parse(request)
    print(requestFromUser)
    serializedUser = RegisterSerializer(register_fromtable, data=requestFromUser)
    print(serializedUser)
    if serializedUser.is_valid():
        print("Data ids valid")
        serializedUser.save()
        return JsonResponse(serializedUser.data)
    return JsonResponse(serializedUser.errors)


@api_view(['DELETE'])

def deletebyId(request,pk):
    print("Entering delete method")
    register_fromtable = Register.objects.get(pk=pk)
    print(register_fromtable)
    register_fromtable.delete()

    # in delete we are not deleting data in table and not mapping into table hence no serializer
    # serialized_data = RegisterSerializer(register_fromtable)
    # serialized_data.delete()
    return JsonResponse({'message':'deleted user successfully'})

@api_view(['POST'])   # for login we use post method
def login(request):
    print("Entrering to login page")
    python_obj = JSONParser().parse(request)
    print(python_obj)
    print(python_obj["email_id"])
    print(python_obj["password"])
    reg_fromTable = Register.objects.filter(email_id=python_obj["email_id"]).filter(password=python_obj["password"])
    print(reg_fromTable)
    serialized_obj = RegisterSerializer(reg_fromTable, many=True)
    print(serialized_obj)
    return JsonResponse(serialized_obj.data, safe=False)



@api_view(['POST'])
# Create your views here.
def create_product(request):
    print("Entering to create new product")
    # return HttpResponse("creating an account")
    python_obj = JSONParser().parse(request)
    print(python_obj)

    # to map python obj to table in db

    serialized_obj = ProductSerializer(data=python_obj)
    print(serialized_obj)
    if serialized_obj.is_valid():
        print("Data is valid")
        serialized_obj.save()
        return JsonResponse(serialized_obj.data)
    else:
        print("Data is invalid")
        return JsonResponse(serialized_obj.errors)

from .models import Product
@api_view(['GET'])
def getProduct(request):
    print("Enterining get user method")
    productFromDb = Product.objects.all()
    print(productFromDb)
    serialize_obj = ProductSerializer(productFromDb, many=True)
    print(serialize_obj)
    return JsonResponse(serialize_obj.data, safe=False)


@api_view(['PUT'])
def updateProduct(request, pk):
    print("Entering to upadatebyId")
    product_fromtable = Product.objects.get(pk=pk)
    print(product_fromtable)
    requestFromUser = JSONParser().parse(request)
    print(requestFromUser)
    serializedUser = ProductSerializer(product_fromtable, data=requestFromUser)
    print(serializedUser)
    if serializedUser.is_valid():
        print("Data ids valid")
        serializedUser.save()
        return JsonResponse(serializedUser.data)
    return JsonResponse(serializedUser.errors)
