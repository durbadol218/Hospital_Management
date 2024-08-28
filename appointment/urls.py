from django.urls import include,path
from rest_framework import routers
from . import views

router = routers.DefaultRouter() # router toiri korlam!
router.register('',views.AppointmentViewSet) # akta antena create korlam!

urlpatterns = [
    path('',include(router.urls)),
    
]
