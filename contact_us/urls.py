from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . views import ContactUsViewset
router = DefaultRouter() #our router

router.register('', ContactUsViewset) # our antena of rounter

urlpatterns = [
    path('',include(router.urls))
]
