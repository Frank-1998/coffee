from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.template import Context, Template
from . serializers import CoffeeSerializerAll
from . serializers import DetailSerializer
from . serializers import AddSerializer
from . models import Coffee


# Create your views here.


#===============================================================================================
'''
give the overview of the api
'GET' method
url: coffeeApi/
'''
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/coffee-list/',
        'Deatail View': '/coffee-detail/<int:id>',
        'Add': '/coffee-add/',
        'Update': '/coffee-update/<int:id>',
        'Delete': '/coffee-delete/<int:id>',

    }

    return Response(api_urls)

'''
Show all the coffee in a list, sorting the ids in aschending order
'GET' method
url: coffeeApi/
'''
# Function to show all coffee
# @api_view(['GET'])
def ShowAll(request):
    total_coffee = Coffee.objects.all().count()
    coffees = Coffee.objects.all().order_by('id')
    serializer = CoffeeSerializerAll(coffees, many=True)
    content = {"total": total_coffee, "coffees": serializer.data}
    return Response(content)

'''
Show details for individual coffee selected using id
'GET' method
'''
# Function to show specific coffee
# @api_view(['GET'])
def ViewCoffee(request, pk):
    try:
        coffee = Coffee.objects.get(id=pk)
        serializer = DetailSerializer(coffee, many=False)
        content = {"name": serializer.data.get('name'), "farm": serializer.data.get('farm'), "region": serializer.data.get('region'), "fermentation": serializer.data.get('fermentation'), "price": float(serializer.data.get('price'))}
        return Response(content, status = 200)
    except:
        return Response(status = 404)

'''
Add new coffee to database
'POST' method
'''
# Function to create coffee
# @api_view(['POST'])
def AddCoffee(request):
    serializer = AddSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        content = {"status":0, "message": "New Coffee added", "id": serializer.data.get('id')}
        return Response(content)



# function to update coffee
# @api_view(['PUT'])
def UpdateCoffee(request, pk):
    try:
        coffee = Coffee.objects.get(id=pk)
        serializer = DetailSerializer(instance=coffee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            content = {"status": 0, "message": "Coffee updated"}
            return Response(content)
    except:
        return Response(status = 404)



# function to modify the fields
# @api_view(['PATCH'])
def ModifyCoffee(request, pk):
    try:
        coffee = Coffee.objects.get(id=pk)
        serializer = DetailSerializer(instance=coffee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            content = {"status": 0, "message": "Coffee modified"}
            return Response(content)
    except:
        return Response(status = 404)



# function to delete coffee
# @api_view(['DELETE'])
def DeleteCoffee(request, pk):
    try:
        coffee = Coffee.objects.get(id=pk)
        coffee.delete()
        content = {"status": 0, "message": "Coffee deleted"}
        return Response(content, status=200)
    except:
        return Response(status=404)


# Function to decide which function to use when no provide
@api_view(['GET', 'POST'])
def APICoffeeNoPk(request):
    if request.method == 'GET':
        return ShowAll(request)
    elif request.method == 'POST':
        return AddCoffee(request)

# Function to decided which function to use when provide id
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def APICoffeePk(request, pk):
    if request.method == 'GET':
        return ViewCoffee(request,pk)
    elif request.method == 'PUT':
        return UpdateCoffee(request, pk)
    elif request.method == 'PATCH':
        return ModifyCoffee(request, pk)
    elif request.method == 'DELETE':
        return DeleteCoffee(request, pk)
