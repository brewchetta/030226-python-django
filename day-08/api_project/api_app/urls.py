from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/mars-rover-parts', views.MarsRoverPartsList.as_view(), name="mars_rover_parts_list"),

    path('api/v1/mars-rover-parts/<int:pk>', views.MarsRoverPartsDetail.as_view(), name="mars_rover_parts_detail"),

    path('parts-index', views.PartsIndex.as_view(), name="parts_index"),

    path('api/v1/rovers', views.RoverList.as_view(), name="rover_list"),
]
