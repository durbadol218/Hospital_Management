from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() #our router

router.register('list', views.DoctorViewset) # our antena of rounter
router.register('specialization', views.SpecializationViewset) # our antena of rounter
router.register('avail_time', views.AvailableTimeViewset) # our antena of rounter
router.register('designation', views.DesignationViewset) # our antena of rounter
router.register('reviews', views.ReviewViewset) # our antena of rounter

urlpatterns = [
    path('',include(router.urls))
]
