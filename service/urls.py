from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . views import ServiceViewset
router = DefaultRouter() #our router

router.register('', ServiceViewset) # our antena of rounter

urlpatterns = [
    path('',include(router.urls))
]
