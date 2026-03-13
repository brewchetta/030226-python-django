from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MarsRoverPart
from .serializers import MarsRoverPartSerializer

# /mars-rover-parts
# the list has two purposes --> GET - show all items
#                           --> POST - create a new item

# MARS ROVER PARTS LIST #
@api_view([ "GET", "POST" ])
def mars_rover_parts_list(request):

    # if this is a GET request -- show all the parts
    if request.method == "GET":
        # get all rover parts
        all_parts = MarsRoverPart.objects.all()
        # plug parts into the serializer --> many=True means we will show many items
        serializer = MarsRoverPartSerializer(all_parts, many=True)
        # serializer.data creates JSON data that we send to the user
        return Response(serializer.data, status=status.HTTP_200_OK)

    # if this is a POST request -- try to make the new item
    if request.method == "POST":
        # format the sent data in a serializer
        serializer = MarsRoverPartSerializer(data=request.data)
        # if valid save it
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if invalid send the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# .mars-rover-parts/:id
# the detail has three purpose --> GET - show the part with the id
#                              --> PUT/PATCH - edit the part with the id
#                              --> DELETE - delete the part with the id

# MARS ROVER PARTS DETAIL #
@api_view([ "GET", "PATCH", "PUT", "DELETE" ])
def mars_rover_parts_detail(request, pk):
    # try to find the rover part first regardless of GET, PATCH, PUT, DELETE
    try:
        found_rover_part = MarsRoverPart.objects.get(pk=pk)
    # give a 404 response if not found
    except MarsRoverPart.DoesNotExist:
        message = { "error": "Unable to find this rover part" }
        return Response( message, status=status.HTTP_404_NOT_FOUND )

    # if we get a PATCH of a PUT -- edit the given item
    if request.method == "PATCH" or request.method == "PUT":
        # create a new instance of the serializer with the original data and the new data that gets sent
        serializer = MarsRoverPartSerializer(found_rover_part, data=request.data)
        # if valid save it
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        # otherwise send the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # if this is a GET request -- show the rover part with a matching pk/id
    if request.method == "GET":
        # put this part's data into the serializer --> format the data so we can send it over the internet
        serializer = MarsRoverPartSerializer(found_rover_part)
        # create a response with the data to send back to the user
        return Response(serializer.data, status=status.HTTP_200_OK)

    # if this is a DELETE request -- delete the item and return an empty response
    if request.method == "DELETE":
        found_rover_part.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    







# APIView is a special view just for API calls
from rest_framework.views import APIView

# CLASS BASED APPROACH #

# MARS ROVER PARTS LIST #
class MarsRoverPartsList(APIView):

    # GET #
    def get(self, request):
        all_parts = MarsRoverPart.objects.all()
        serializer = MarsRoverPartSerializer(all_parts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST #
    def post(self, request):
        serializer = MarsRoverPartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarsRoverPartsDetail(APIView):

    # to share the found part with the get, patch, delete
    def find_part(self, pk):
        try:
            return MarsRoverPart.objects.get(pk=pk)
        except MarsRoverPart.DoesNotExist:
            message = { "error": "Unable to find this rover part" }
            return Response( message, status=status.HTTP_404_NOT_FOUND )

    # GET #
    def get(self, request, pk):
        found_rover_part = self.find_part(pk)
        serializer = MarsRoverPartSerializer(found_rover_part)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PATCH #
    def patch(self, request, pk):
        found_rover_part = self.find_part(pk)
        serializer = MarsRoverPartSerializer(found_rover_part, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE #
    def delete(self, request, pk):
        found_rover_part = self.find_part(pk)
        found_rover_part.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

# NORMAL VIEW #

from django.views.generic import TemplateView

class PartsIndex(TemplateView):
    template_name = "api_app/parts_index.html"


from .models import Rover
from .serializers import RoverSerializer

class RoverList(APIView):
    
    # GET --> localhost:8000/api/v1/rovers
    def get(self, request):
        all_rovers = Rover.objects.all()
        serializer = RoverSerializer(all_rovers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    



# FOR USING PUBLIC APIS WITH API KEYS

from django.conf import settings
import requests

MARS_WEATHER_URL = f"https://api.nasa.gov/insight_weather/?api_key={settings.NASA_API_KEY}&feedtype=json&ver=1.0"


def mars_weather(request):
    response = requests.get(MARS_WEATHER_URL)
    # if the response came back with a 200
    if response.ok:
        # parse out data so it can be used
        data = response.json()
        context = { "data": data }
        return render(request, "api_app/mars_weather.html", context)

    # if response wasn't ok (bad connection, server issues, etc.)
    else:
        context = { "errors": "Could not get weather data, please try again later" }
        return render(request, "api_app/mars_weather.html", context)